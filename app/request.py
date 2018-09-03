from app import app
import urllib.request, json
from .model import Source, Article

# Source = source.Source

# Getting api key
api_key = None
# print(api_key)
# Getting the source base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.conifig['NEWS_SOURCE_API_KEY']
    base_url = app.config['NEWS_SOURCE_API_BASE_URL']
    article_url = app.config['https://newsapi.org/v2/top-headlines?sources={}&apiKey={}']


# print(base_url)

def get_source():
    '''
    funtion that gets the json response from our request
    :return:
    '''
    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results


# Article = articles.Article


def process_results(source_list):
    '''
    fxn that processes the news results and transfor,ms the json reponse to a list of objects
    :param source_list:
    :return:
    '''
    source_results = []
    for source_item in source_list:
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item.get('description')
        rt = source_item.get('id')

        source_data = Source(name, url, description, rt)
        source_results.append(source_data)

    return source_results


def get_article(name):
    source_articles_url = article_url.format(name, api_key, )

    with urllib.request.urlopen(source_articles_url) as url:
        articles = url.read()
        articles_response = json.loads(articles)
        # print(articles_response)

        articles_list = None

        if articles_response['articles']:
            article_json = articles_response['articles']
            articles_list = process_articles(article_json)

    return articles_list


def process_articles(articles):
    article_list = []
    for article in articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')

        article_data = Article(author, title, description, url, urlToImage)

        article_list.append(article_data)

    return article_list
