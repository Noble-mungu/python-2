import os
class  Config:
    '''
    General configuration parnet class

    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}'
    NEWS_ARTICLES_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}'
class ProdConfig(Config):

    '''
    Production configuration child class
    

    Args:
    Config:The parent configuration class with general configuration settings
     '''
    pass

class DevConfig(Config):
     '''
     Development configuration child class

     Args:
     Config:The parent configuration class with General settings

     '''     
     DEBUG = True
config_options = {
    # A to help us access different configuration option classes.
'development' : DevConfig,
'production' : ProdConfig
} 


