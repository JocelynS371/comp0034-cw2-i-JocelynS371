from pathlib import Path
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_app.config import DevelopmentConfig
from flask_login import LoginManager


PROJECT_ROOT = Path(__file__).parent
db = SQLAlchemy()
login_manager = LoginManager()


def internal_server_error(e):
    """
    Handles error when server is unresponsivw
    """
    return render_template("error-500.html"), 500


def page_not_found(e):
    """
    Handles error when a non-existent URL is entered
    """
    return render_template("error-404.html"), 404


def unauthorized(e):
    """
    Handles error when user tries to access content without login
    """
    return render_template("error-401.html"), 401


# config is not working with the terminal for unknown reason
# if app is to be opened in terminal,
# swap the commented code and the previous line of code
# def create_app():
def create_app(config_class):

    """Create and configure the Flask app"""

    app = Flask(__name__)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(401, unauthorized)
    app.config.from_object(config_class)
    # app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from . import routes
        from .models import Data, User
        db.create_all()

    return app
