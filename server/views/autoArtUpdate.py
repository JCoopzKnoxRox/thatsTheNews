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
    verge_paper = newspaper.build("https://www.theverge.com/",  memorize_articles=True, language = 'en')
    print("verge_paper built", file=sys.stderr)
    techP = [verge_paper]
    espn_paper = newspaper.build("https://www.espn.com/",  memorize_articles=True, language = 'en')
    print("espn_paper built", file=sys.stderr)
    sportP = [espn_paper]
    et_paper = newspaper.build("https://ew.com/",  memorize_articles=True, language = 'en')
    print("ew_paper built", file=sys.stderr)
    entertainmentP = [et_paper]
    crypto_paper = newspaper.build("https://cryptonews.com/",  memorize_articles=True, language = 'en')
    print("crypto_paper built", file=sys.stderr)
    cryptoP = [crypto_paper]
    climate_paper = newspaper.build("https://www.climatechangenews.com/",  memorize_articles=True, language = 'en')
    print("climate_paper built", file=sys.stderr)
    climateP = [climate_paper]
    print("all papers built", file=sys.stderr)
    count = 0
    article_list = []
    print("Starting pool threading", file=sys.stderr)
    news_pool.set(papers, threads_per_source=1000)
    news_pool.join()
    news_pool.set(techP, threads_per_source=1000)
    news_pool.join()
    news_pool.set(sportP, threads_per_source=1000)
    news_pool.join()
    news_pool.set(entertainmentP, threads_per_source=1000)
    news_pool.join()
    news_pool.set(cryptoP, threads_per_source=1000)
    news_pool.join()
    news_pool.set(climateP, threads_per_source=1000)
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
            elif "buisness" in news.url:
                news.parse()
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "buisness",
                    text = news.text,
                    title = news.title,
                    date = Date #.strftime("%m/%d/%Y")
                    ).save()
            elif "covid" in news.url or "corona" in news.url:
                news.parse()
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "covid",
                    text = news.text,
                    title = news.title,
                    date = Date #.strftime("%m/%d/%Y")
                    ).save()
                count += 1
    for build in techP:
        for news in (build.articles):
            news.parse()
            if "#comments" not in news.url:
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "tech",
                    text = news.text,
                    title = news.title,
                    date = Date #.strftime("%m/%d/%Y")
                    ).save()
    for build in sportP:
        for news in (build.articles):
            news.parse()
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "sports",
                text = news.text,
                title = news.title,
                date = Date #.strftime("%m/%d/%Y")
                ).save()
    for build in entertainmentP:
        for news in (build.articles):
            news.parse()
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "entertainment",
                text = news.text,
                title = news.title,
                date = Date #.strftime("%m/%d/%Y")
                ).save()
    for build in cryptoP:
        for news in (build.articles):
            news.parse()
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "crypto",
                text = news.text,
                title = news.title,
                date = Date #.strftime("%m/%d/%Y")
                ).save()
    for build in climateP:
        for news in (build.articles):
            news.parse()
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "climate",
                text = news.text,
                title = news.title,
                date = Date #.strftime("%m/%d/%Y")
                ).save()            
    print("Articles saved in mongodb", file=sys.stderr)

#Schedule the above function to run every hour to look for new news articles
print("instantiating scheduler", file=sys.stderr)
scheduler = BackgroundScheduler()
print("adding job to scheduler", file=sys.stderr)
scheduler.add_job(auto_article_go_getter, 'interval', next_run_time=datetime.datetime.now(), hours=1) 
print("starting scheduler", file=sys.stderr)
scheduler.start()
print("finished schedule", file=sys.stderr)