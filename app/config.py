class Config:
    '''
    configuration of the parent class general/global
    '''
    NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'


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
