import pytest
from . import create_app, config, data, user
from selenium.webdriver.chrome.options import Options
from dash.testing.application_runners import import_app


@pytest.fixture(scope="session")
def app():
    """Create a Flask app configured for testing"""
    app = create_app(config.TestConfig)
    yield app


@pytest.fixture(scope="function")
def test_client():
    """ Flask test client within an application context. """
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def new_user():
    User = user('admin_test', 'admin_test')
    return User



def pytest_setup_options():
    options = Options()
    # Uncomment the following if testing on GitHub actions, the browser needs to run in headless mode
    #options.add_argument('--disable-gpu')
    #options.add_argument('--headless')
    return options