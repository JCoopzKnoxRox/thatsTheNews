from schema import Schema, And

import utils
from app import app
from flask import jsonify, request
from models import Post, User, Comment, Subvue, NewsArticle
from mongoengine.errors import ValidationError
from authorization import login_required
import requests
import json
import newspaper
from newspaper import Article
from newspaper import Config
from newspaper import news_pool
import sys
#import nlp

@app.route("/api/posts")
def posts_index():
    posts = Post.objects().order_by("-created")
    return jsonify([post.to_public_json() for post in posts])

@app.route("/api/posts", methods=["POST"])
#@login_required
def posts_create(username: str):
    schema = Schema({
        "title": And(str, len, error="Title not specified"),
        "subvue": And(str, len, error="Subvue not specified"),
        "content": And(str, len, error="Content not specified"),
    })
    form = {
        "title": request.form.get("title"),
        "subvue": request.form.get("subvue"),
        "content": request.form.get("content")
    }
    validated = schema.validate(form)

    subvue_permalink = validated["subvue"]
    subvue = Subvue.objects(permalink__iexact=subvue_permalink).first()
    if not subvue:
        return jsonify({"error": f"Subvue '{subvue_permalink}' not found"}), 404

    user = User.objects(username=username).first()

    image = request.files.get("image")
    if image:
        image_filename = utils.save_image()

    else:
        image_filename = None

    post = Post(
        title=validated["title"],
        subvue=subvue,
        content=validated["content"],
        user=user,
        comments=[],
        image=image_filename
    ).save()

    return jsonify(post.to_public_json())

@app.route("/api/newsarticle/<string:id>")
def newsarticle_index(id : str):
    cnn_paper = newspaper.build("https://www.cnn.com",  memorize_articles=True, language = 'en')
    nbc_paper = newspaper.build("https://www.nbcnews.com",  memorize_articles=True, language = 'en')
    nyt_paper = newspaper.build("https://www.nytimes.com/",  memorize_articles=False, language = 'en')
    apn_paper = newspaper.build("https://apnews.com/",  memorize_articles=False, language = 'en')
    abc_paper = newspaper.build("https://abcnews.go.com/",  memorize_articles=False, language = 'en')
    papers = [cnn_paper, nbc_paper, nyt_paper, apn_paper, abc_paper]
    print("all built", file=sys.stderr)
    #newarticles = NewsArticle.objects().order_by("-created")
    #return jsonify([article.to_public_json() for article in newarticles])
    count = 0
    #sort the API return list with arguments: everything?q=Apple&from=2021-04-16&sortBy=popularity
    article_list = []
    if id == "right":
      #article_list = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #news_json = json.loads(article_list.text)
        #for article in article_list.articles:
           #print(article.url, file=sys.stderr)
        news_pool.set(papers, threads_per_source=1000)
        news_pool.join()
        #print(article_list.articles[0].url, file=sys.stderr)
        #for article in article_list.articles:
            #article.parse()
            #print(article.url + "\n", file=sys.stderr)
            #print(article.text + "\n\n\n\n\n\n\n", file=sys.stderr)
        #first_article = article_list.articles[3]
        #first_article.parse()
        #print(first_article.text, file=sys.stderr)
        #article_list = requests.get("http://newsapi.org/v2/everything?q=Stocks&sortBy=popularity&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        for build in papers:
            for news in (build.articles):
                #len(news_json['articles'])
                    #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
                    #config = Config()
                    #config.browser_user_agent = user_agent
                    #print(news.url, file=sys.stderr)
                    if "politics" in news.url:
                        news.parse()
                        article = NewsArticle(
                            #128 characters is the max string length in MONGODB
                            link = news.url,
                            image = news.top_image,
                            #wing = news['source']['name'][:128],
                            wing = "political",
                            #text = news['description'][:100]
                            text = news.text
                            ).save()
                        count += 1
        artic = []
        for article in NewsArticle.objects():
            if (article.wing == "political"):
                print(article.link, file=sys.stderr)
                artic.append(article)
        return jsonify([article.to_public_json() for article in artic])
    elif id == "left":
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #news_json = json.loads(article_list.text)
        #for article in article_list.articles:
           #print(article.url, file=sys.stderr)
        news_pool.set(papers, threads_per_source=1000)
        news_pool.join()
        #print(article_list.articles[0].url, file=sys.stderr)
        #for article in article_list.articles:
            #article.parse()
            #print(article.url + "\n", file=sys.stderr)
            #print(article.text + "\n\n\n\n\n\n\n", file=sys.stderr)
        #first_article = article_list.articles[3]
        #first_article.parse()
        #print(first_article.text, file=sys.stderr)
        #article_list = requests.get("http://newsapi.org/v2/everything?q=Stocks&sortBy=popularity&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        for build in papers:
            for news in (build.articles):
                #len(news_json['articles'])
                    #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
                    #config = Config()
                    #config.browser_user_agent = user_agent
                    if "politics" in news.url:
                        news.parse()
                        article = NewsArticle(
                            #128 characters is the max string length in MONGODB
                            link = news.url,
                            image = news.top_image,
                            #wing = news['source']['name'][:128],
                            wing = "political",
                            #text = news['description'][:100]
                            text = news.text
                            ).save()
                        print(news.movies, file=sys.stderr)
                        count += 1
        artic = []
        for article in NewsArticle.objects():
            if (article.wing == "political"):
                artic.append(article)
        return jsonify([article.to_public_json() for article in artic])
    elif id == "home":
        article_list = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        news_json = json.loads(article_list.text)
        #article_list = requests.get("http://newsapi.org/v2/everything?q=Stocks&sortBy=popularity&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        for news in (news_json['articles']):
            #len(news_json['articles'])
            if count<len(news_json['articles']):
                #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
                #config = Config()
                #config.browser_user_agent = user_agent
                art = Article(news['url'])
                art.download()
                art.parse()
                article = NewsArticle(
                    #128 characters is the max string length in MONGODB
                    link = news['url'],
                    image = news['urlToImage'],
                    #wing = news['source']['name'][:128],
                    wing = news['title'],
                    #text = news['description'][:100]
                    text = art.text
                    ).save()
                count += 1
        artic = NewsArticle.objects()
        return jsonify([article.to_public_json() for article in artic])
    elif id == "stocks":
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?country=us&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        #article_list = requests.get("http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        article_list = requests.get("http://newsapi.org/v2/everything?q=Stocks&sortBy=popularity&apiKey=8d4f60725e81455fa280396b8e9c64a2")
        news_json = json.loads(article_list.text)
        for news in (news_json['articles']):
            #len(news_json['articles'])
            if count<len(news_json['articles']):
                #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
                #config = Config()
                #config.browser_user_agent = user_agent
                art = Article(news['url'])
                art.download()
                art.parse()
                article = NewsArticle(
                    #128 characters is the max string length in MONGODB
                    link = news['url'],
                    image = news['urlToImage'],
                    #wing = news['source']['name'][:128],
                    wing = news['title'],
                    #text = news['description'][:100]
                    text = art.text
                    ).save()
                count += 1
        artic = NewsArticle.objects()
        return jsonify([article.to_public_json() for article in artic])
    else:
        return "hahaha"
            

@app.route("/api/newsarticle", methods=["POST"])
def newsarticle_create():
            article = NewsArticle(
                link = "test link",
                wing = "test wing",
                text = "some sample text"
                ).save()
            return article

@app.route("/api/posts/id/<string:id>")
def posts_item(id: str):
    try:
        post = Post.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    return jsonify(post.to_public_json())


@app.route("/api/posts/user/<string:username>")
def posts_user(username: str):
    try:
        user = User.objects(username=username).first()
    except ValidationError:
        return jsonify({"error": "User not found"}), 404

    posts = Post.objects(user=user).order_by("-created")

    return jsonify([post.to_public_json() for post in posts])


@app.route("/api/posts/id/<string:id>", methods=["DELETE"])
@login_required
def posts_delete(username: str, id: str):
    try:
        post = Post.objects(pk=id).first()

        # If post has alreay been deleted
        if not post:
            raise ValidationError
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    # Check whether action was called by creator of the post
    if username != post.user.username:
        return jsonify({"error": "You are not the creator of the post"}), 401

    post_info = post.to_public_json()

    post.delete()

    return jsonify(post_info)


@app.route("/api/posts/<string:id>/comments", methods=["POST"])
@login_required
def posts_create_comment(username: str, id: str):
    schema = Schema({
        "content": And(str, len, error="No content specified")
    })
    validated = schema.validate(request.json)

    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()
    comments = post.comments
    comments.append(Comment(user=user, content=validated["content"]))
    post.save()

    return jsonify([comment.to_public_json() for comment in post.comments][::-1])


@app.route("/api/posts/<string:id>/upvote", methods=["POST"])
@login_required
def posts_upvote(username: str, id: str):
    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()

    upvotes = post.upvotes
    downvotes = post.downvotes

    if username in [u["username"] for u in upvotes]:
        # User already upvotes
        upvote_index = [d.username for d in upvotes].index(username)
        upvotes.pop(upvote_index)
    elif username in [u["username"] for u in downvotes]:
        # User already downvoted
        downvote_index = [d.username for d in downvotes].index(username)
        downvotes.pop(downvote_index)
        upvotes.append(user)
    else:
        upvotes.append(user)

    post.save()

    return jsonify({
        "upvotes": post.to_public_json()["upvotes"],
        "downvotes": post.to_public_json()["downvotes"]
    })


@app.route("/api/posts/<string:id>/downvote", methods=["POST"])
@login_required
def posts_downvote(username: str, id: str):
    try:
        post = Post.objects(pk=id).first()
    except ValidationError:
        return jsonify({"error": "Post not found"}), 404

    user = User.objects(username=username).first()

    upvotes = post.upvotes
    downvotes = post.downvotes

    if username in [u["username"] for u in downvotes]:
        # User already upvotes
        downvote_index = [d.username for d in downvotes].index(username)
        downvotes.pop(downvote_index)
    elif username in [u["username"] for u in upvotes]:
        upvote_index = [d.username for d in upvotes].index(username)
        upvotes.pop(upvote_index)
        downvotes.append(user)
    else:
        downvotes.append(user)

    post.save()

    return jsonify({
        "upvotes": post.to_public_json()["upvotes"],
        "downvotes": post.to_public_json()["downvotes"]
    })
