class Config:
    
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    API_KEY = "4100452f82034e358ce28c3cca4a97b2"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options= {
    'development': DevConfig,
    'production': ProdConfig
}