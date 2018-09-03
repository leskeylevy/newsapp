import os


class Config:
    '''
    configuration of the parent class general/global
    '''
    NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    api_key = os.environ.get('NEWS_SOURCE_API_KEY')


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


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
