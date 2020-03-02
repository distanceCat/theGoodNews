# powered by newsapi.org
# import requests
# import json
# import sentiment_analyser
import config
import sqlite3
import datetime
from newsapi import NewsApiClient

def fetch_news():
    newsapi = NewsApiClient(api_key=config.newsapi_key)

    news_feed_json = newsapi.get_top_headlines(country='de')
    articles = []
    for article in news_feed_json["articles"]:
        articles.append(article["title"])
        print(article["title"])

    # sentiment_analyser.SentimentAnalyser.sample_analyze_sentiment(articles[0])
    # print(news_feed_json["articles"])
    # print(response.json())
    return articles

def store_titles(articles):
    conn = sqlite3.connect(".\data\storage.db")
    c = conn.cursor()
    dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    the_date = datetime.datetime.now().strftime("%Y%m%d")
    c.execute("INSERT INTO good_news_short(datetime, date, title) VALUES (?, ?, ?)", (dt, the_date, articles[0]))
    conn.commit()
    conn.close()



if __name__ == '__main__':
    fetch_news()
    articles = fetch_news()
    store_titles(articles)
