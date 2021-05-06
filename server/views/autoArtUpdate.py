import json
import sys
import newspaper
import requests
import utils
import datetime
from app import app
from authorization import login_required
from flask import jsonify, request
from models import NewsArticle
from mongoengine.errors import ValidationError
from newspaper import Article, Config, news_pool
from schema import And, Schema
from apscheduler.schedulers.background import BackgroundScheduler
from time import strftime



def auto_article_go_getter():
    print("starting builds ", file=sys.stderr)
    cnn_paper = newspaper.build("https://www.cnn.com",  memorize_articles=True, language = 'en')
    print("cnn_paper built", file=sys.stderr)
    nbc_paper = newspaper.build("https://www.nbcnews.com",  memorize_articles=True, language = 'en')
    print("nbc_paper built", file=sys.stderr)
    nyt_paper = newspaper.build("https://www.nytimes.com/",  memorize_articles=True, language = 'en')
    print("nyt_paper built", file=sys.stderr)
    apn_paper = newspaper.build("https://apnews.com/",  memorize_articles=True, language = 'en')
    print("apn_paper built", file=sys.stderr)
    abc_paper = newspaper.build("https://abcnews.go.com/",  memorize_articles=True, language = 'en')
    print("abc_paper built", file=sys.stderr)
    papers = [cnn_paper, nbc_paper, nyt_paper, apn_paper, abc_paper]
    print("all papers built", file=sys.stderr)
    count = 0
    article_list = []
    print("Starting pool threading", file=sys.stderr)
    news_pool.set(papers, threads_per_source=1000)
    news_pool.join()
    print("Saving articles to mongodb", file=sys.stderr)
    for build in papers:
        for news in (build.articles):
            Date = news.publish_date
            if "politics" in news.url:
                news.parse()
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "political",
                    text = news.text,
                    title = news.title,
                    date = Date #.strftime("%m/%d/%Y")
                    ).save()
            elif "stock" in news.text:
                news.parse()
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "stocks",
                    text = news.text,
                    title = news.title,
                    date = Date #.strftime("%m/%d/%Y")
                    ).save()
                count += 1
    print("Articles saved in mongodb", file=sys.stderr)

#Schedule the above function to run every hour to look for new news articles
print("instantiating scheduler", file=sys.stderr)
scheduler = BackgroundScheduler()
print("adding job to scheduler", file=sys.stderr)
scheduler.add_job(auto_article_go_getter, 'interval', next_run_time=datetime.datetime.now(), hours=1) 
print("starting scheduler", file=sys.stderr)
scheduler.start()
print("finished schedule", file=sys.stderr)