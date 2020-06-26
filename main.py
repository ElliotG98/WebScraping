from flask import Flask, jsonify, render_template, request
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

app = Flask(__name__)
app.config['DEBUG'] = True

# GLOBAL VARIABLES
data_news = {'articles': []}
url = "https://news.google.com/rss"

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


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/articles/all', methods=['GET'])
def api_all():
    news(url)
    return jsonify(data_news)

@app.route('/api/articles', methods=['GET'])
def api_counter():
    if 'count' in request.args:
        counter = int(request.args['count'])
    else:
        return "Error: No count field provided. Please specify a query parameter."

    news(url, counter)
    return jsonify(data_news)