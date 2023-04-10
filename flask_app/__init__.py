from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


PROJECT_ROOT = Path(__file__).parent
db = SQLAlchemy()


def create_app():

    """Create and configure the Flask app"""

    app = Flask(__name__)
    app.config.update(
        TESTING=True,
        SECRET_KEY='saULPgD9XU8vzLVk7kyLBw',
        SQLALCHEMY_DATABASE_URI="sqlite:///" + str(
            PROJECT_ROOT.joinpath("data", "data.db")),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
        )
    db.init_app(app)
    # Include the routes from routes.py
    with app.app_context():
        from . import routes
        from .models import data, user
        db.create_all()

    return app
