import pytest
from flask import current_app as app
from flask_app.models import Data, User
from flask_app import create_app, db
from flask_app.config import Config, ProductionConfig, DevelopmentConfig, TestingConfig
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(TestingConfig)
    yield app


@pytest.fixture(scope="function")
def test_client(app):
    """ Flask test client within an application context. """
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope="function")
def user(app, test_client):
    with app.app_context():
        with app.test_request_context():
            test_client.post('/register', data=dict(username='dummy', password='dummy'))
            user = User.query.filter_by(username='dummy').first()
            yield user
            db.session.delete(user)
            db.session.commit()


@pytest.hookimpl(optionalhook=True) 
def pytest_setup_options():
    options = Options()
    #Uncomment the following if testing on GitHub actions, the browser needs to run in headless mode
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    return options