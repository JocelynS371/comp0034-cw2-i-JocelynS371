from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_app.config import Config, ProductionConfig, DevelopmentConfig, TestingConfig


PROJECT_ROOT = Path(__file__).parent
db = SQLAlchemy()

# config is not working with the terminal for unknown reason
# if app is to be opened in terminal, 
# swap the commented code and the previous line of code
def create_app(config_class):
#def create_app(): 
    """Create and configure the Flask app"""

    app = Flask(__name__)
    app.config.from_object(config_class)
    #app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        from . import routes
        from .models import data, user
        db.create_all()

    return app
