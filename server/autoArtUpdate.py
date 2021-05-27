# importing libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import json
import sys
import newspaper
import requests
import datetime
from mongoengine.errors import ValidationError
from newspaper import Article, Config, news_pool
from schema import And, Schema
from apscheduler.schedulers.background import BackgroundScheduler
from time import strftime
from flask import jsonify, request
from app import app
from authorization import login_required
from models import NewsArticle
import utils

def auto_article_go_getter():
    print("starting builds ", file=sys.stderr)
    cnn_paper = newspaper.build("https://www.cnn.com",  memorize_articles=True, language = 'en')
    print("cnn_paper built", file=sys.stderr)
    nbc_paper = newspaper.build("https://www.nbcnews.com",  memorize_articles=True, language = 'en')
    #print("nbc_paper built", file=sys.stderr)
    #nyt_paper = newspaper.build("https://www.nytimes.com/",  memorize_articles=True, language = 'en')
    #print("nyt_paper built", file=sys.stderr)
    apn_paper = newspaper.build("https://apnews.com/",  memorize_articles=True, language = 'en')
    print("apn_paper built", file=sys.stderr)
    abc_paper = newspaper.build("https://abcnews.go.com/",  memorize_articles=True, language = 'en')
    print("abc_paper built", file=sys.stderr)
    papers = [cnn_paper, nbc_paper, apn_paper, abc_paper]
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
    print("Starting pool for papers", file=sys.stderr)
    news_pool.set(papers, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for papers", file=sys.stderr)
    print("Starting pool for techp", file=sys.stderr)
    news_pool.set(techP, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for techp", file=sys.stderr)
    print("Starting pool for sportp", file=sys.stderr)
    news_pool.set(sportP, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for sportp", file=sys.stderr)
    print("Starting pool for entertainmentp", file=sys.stderr)
    news_pool.set(entertainmentP, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for entertainmentp", file=sys.stderr)
    print("Starting pool for cryptop", file=sys.stderr)
    news_pool.set(cryptoP, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for cryptop", file=sys.stderr)
    print("Starting pool for climatep", file=sys.stderr)
    news_pool.set(climateP, threads_per_source=1000)
    news_pool.join()
    print("Finished pool threading for climatep", file=sys.stderr)
    print("Saving articles to mongodb", file=sys.stderr)
    for build in papers:
        for news in (build.articles):
            if "politics" in news.url and "cnnespanol" not in news.url:
                news.parse()
                #call on text summarizer with text of article
                textSum = text_summarizer(news.text)
                if "apnews.com" in news.url:
                    textSum = news.text
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "political",
                    #text = news.text,
                    text = textSum,
                    title = news.title
                    ).save()
            #email_services = ["hotmail", "gmail", "yahoo"] 
            #email_contains_service = any(email_service in user_email for email_service in email_services)
            elif ["stock", "net", "loss", "Q1", "Q2", "Q3", "Q4", "Gain"] in word_tokenize(news.text):
                news.parse()
                #call on text summarizer with text of article
                textSum = text_summarizer(news.text)
                if "apnews.com" in news.url:
                    textSum = news.text
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "buisness",
                    text = textSum,
                    title = news.title
                    ).save()
            elif "covid" in news.url or "corona" in news.url:
                news.parse()
                #call on text summarizer with text of article
                textSum = text_summarizer(news.text)
                if "apnews.com" in news.url:
                    textSum = news.text
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "covid",
                    text = textSum,
                    title = news.title
                    ).save()
                count += 1
    for build in techP:
        for news in (build.articles):
            news.parse()
            #call on text summarizer with text of article
            textSum = text_summarizer(news.text)
            if "apnews.com" in news.url:
                    textSum = news.text
            if "#comments" not in news.url:
                article = NewsArticle(
                    link = news.url,
                    image = news.top_image,
                    wing = "tech",
                    text = textSum,
                    title = news.title
                    ).save()
    for build in sportP:
        for news in (build.articles):
            news.parse()
            #call on text summarizer with text of article
            textSum = text_summarizer(news.text)
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "sports",
                text = textSum,
                title = news.title
                ).save()
    for build in entertainmentP:
        for news in (build.articles):
            news.parse()
            #call on text summarizer with text of article
            textSum = text_summarizer(news.text)
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "entertainment",
                text = textSum,
                title = news.title
                ).save()
    for build in cryptoP:
        for news in (build.articles):
            news.parse()
            #call on text summarizer with text of article
            textSum = text_summarizer(news.text)
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "crypto",
                text = textSum,
                title = news.title
                ).save()
    for build in climateP:
        for news in (build.articles):
            news.parse()
            #call on text summarizer with text of article
            textSum = text_summarizer(news.text)
            article = NewsArticle(
                link = news.url,
                image = news.top_image,
                wing = "climate",
                text = textSum,
                title = news.title
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


def text_summarizer(text):     
    print("Starting Text Summarizer", file=sys.stderr) 
    if (len(text) <= 0): 
        return text
    else:   
        # Tokenizing the text
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        #print(text, file=sys.stderr) 
        print(text +"\n \n \n \n \n \n \n \n \n", file=sys.stderr)
        
        # Creating a frequency table to keep the 
        # score of each word
        
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        
        # Creating a dictionary to keep the score
        # of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        
        
        
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        
        # Average value of a sentence from the original text
        
        average = int(sumValues / len(sentenceValue))
        
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence

        print(summary + "\n \n \n", file=sys.stderr) 
        return summary

if __name__ == "__main__": 
    auto_article_go_getter()