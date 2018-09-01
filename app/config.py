import os
class Config:
    '''
    configuration of the parent class general/global
    '''
    NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    api_key = os.environ.get('95992d07cc4345d9bdcdccea9dcdd645')

class ProdConfig(Config):
    '''
    production of the child class configuration

    Args:
        config:parent class with global configuraation

    '''
    pass


class DevConfig(Config):
    '''
    Development configuation chilldcls
    '''
    DEBUG = True
