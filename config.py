OPENAI_API_KEY = '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'

class Config(object):
    TESTING = False
    DEBUG = True

class DevelopmentConfig(Config):
    SECRET_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}