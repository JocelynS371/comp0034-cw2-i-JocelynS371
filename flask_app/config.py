from flask import current_app as app
from pathlib import Path

"""Flask config class."""
PROJECT_ROOT = Path(__file__).parent

class Config(object):
    SECRET_KEY = "saULPgD9XU8vzLVk7kyLBw"
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///" + str(
    PROJECT_ROOT.joinpath("data", "data.db"))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

