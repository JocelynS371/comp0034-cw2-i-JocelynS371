"""Flask config class."""


class Config(object):
    #app.config["SECRET_KEY"] = "saULPgD9XU8vzLVk7kyLBw"
    pass

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass