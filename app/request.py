from app import app
import urllib.request, json
from .models import source

Source = source.Source

# Getting api key
api_key = '95992d07cc4345d9bdcdccea9dcdd645'
# print(api_key)
# Getting the source base url
base_url = app.config["NEWS_SOURCE_API_BASE_URL"]
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

        source_data = Source(name, url, description)
        source_results.append(source_data)

    return source_results
