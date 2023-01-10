OPENAI_API_KEY = 'enter-api-key'

class Config(object):
    TESTING = False
    DEBUG = True

class DevelopmentConfig(Config):
    SECRET_KEY = 'secret-key'

config = {
    'developmet': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}