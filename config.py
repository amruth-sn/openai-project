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
