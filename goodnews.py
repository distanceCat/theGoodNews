# powered by newsapi.org
import requests
import json
import sentiment_analyser


def fetchNews():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=de&'
           'apiKey=ad803c9cd6f144a287f50bdbd3e5a502')
    response = requests.get(url)
    news_feed_json = response.json()
    articles = []
    for article in news_feed_json["articles"]:
        articles.append(article["title"])
        print(article["title"])

    sentiment_analyser.SentimentAnalyser.sample_analyze_sentiment(articles[0])

    # print(news_feed_json["articles"])
    # print(response.json())


if __name__ == '__main__':
    fetchNews()
