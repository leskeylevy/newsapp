class Config:
    '''
    configuration of the parent class genaral/global
    '''
    NEWS_SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'


class ProdConfig(config):
    '''
    production of the child class configuration

    Args:
        config:parent class with global configuraation

    '''
    pass

class DevConfig(config):
    '''
    Development configuation chilldcls
    '''
    DEBUG =True