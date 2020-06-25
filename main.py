from flask import Flask
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

app = Flask(__name__)

def news(xml_news_url, counter):
    context = ssl._create_unverified_context()
    response = urlopen(xml_news_url, context=context)
    xml_page = response.read()
    response.close()

    soup_page = soup(xml_page, 'xml')
    news_list = soup_page.find_all('item', limit=counter)


@app.route('/')
def home():
    return 'Hello, world'