from flask import current_app as app
from pathlib import Path

"""Flask config class."""
PROJECT_ROOT = Path(__file__).parent

class Config(object):
    """
    Base config
    """
    SECRET_KEY = "saULPgD9XU8vzLVk7kyLBw"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True
    WTF_CSRF_ENABLED = True


class ProductionConfig(Config):
    """
    Config for deployment, not implemented
    """
    pass


class DevelopmentConfig(Config):
    """
    development config, use local database
    """
    SQLALCHEMY_DATABASE_URI="sqlite:///" + str(
    PROJECT_ROOT.joinpath("data", "data.db"))


class TestingConfig(Config):
    """
    Testing config, testing toggled true and database created in memory
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

