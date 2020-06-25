from flask import Flask, jsonify
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

app = Flask(__name__)
app.config['DEBUG'] = True

# GLOBAL VARIABLES
data_news = {'articles': []}
url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"

def news(xml_news_url, counter=20):
    context = ssl._create_unverified_context()
    response = urlopen(xml_news_url, context=context)
    xml_page = response.read()
    response.close()

    soup_page = soup(xml_page, 'xml')
    news_list = soup_page.find_all('item', limit=counter)

    for article in news_list:
        art_dict = {'title': article.title.text, 'pubDate': article.pubDate.text, 'link': article.link.text}
        data_news['articles'].append(art_dict)


@app.route('/', methods=['GET'])
def home():
    news(url, 3)
    return "<h1>API</h1><p>This is going to be where my api data sits</p>"

@app.route('/api/articles/all', methods=['GET'])
def api_all():
    news(url)
    return jsonify(data_news)