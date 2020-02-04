# powered by newsapi.org
import requests
# import json
# import sentiment_analyser
import sqlite3
import datetime

def fetch_news():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=de&'
           'apiKey=ad803c9cd6f144a287f50bdbd3e5a502')
    response = requests.get(url)
    news_feed_json = response.json()
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
    c.execute("INSERT INTO good_news_short(date, title) VALUES (?, ?)", (dt, articles[0]))
    conn.commit()
    conn.close()



if __name__ == '__main__':
    fetch_news()
    articles = fetch_news()
    store_titles(articles)
