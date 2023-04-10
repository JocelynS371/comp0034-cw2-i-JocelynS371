from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.config import Config, ProductionConfig, DevelopmentConfig, TestingConfig


PROJECT_ROOT = Path(__file__).parent
db = SQLAlchemy()


def create_app(config_class):

    """Create and configure the Flask app"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config.from_object(config_class)
    db.init_app(app)
    # Include the routes from routes.py
    with app.app_context():
        from . import routes
        from .models import data, user
        db.create_all()

    return app
