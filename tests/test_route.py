import pytest
import flask_app
from flask_login import login_user

@pytest.mark.parametrize('route, expected', [
    ('/', 200),
    ('/login', 200), 
    ('/register', 200), 
    ('/logout', 401),
    ('/data-entry', 401),
    ('/predict', 401)
    ])
def test_route_without_login(test_client, route, expected):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made without login
    WHEN the route does not require login
    THEN the status code should be 200"
    WHEN the route require login
    THEN the status code should be 401"
    """
    response = test_client.get(route)
    assert response.status_code == expected


@pytest.mark.parametrize('route, expected', [
    ('/', 200),
    ('/login', 200), 
    ('/register', 200),
    ('/logout', 200), 
    ('/data-entry', 200),
    ('/predict', 200)
    ])
def test_route_with_login(app,test_client,user, route, expected):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made by login user
    THEN all the status code should be 200"
    """
    with app.app_context():
        with app.test_request_context():
            test_client.post('/register', data=dict(username='dummy', password='dummy'))
            test_client.post('/login', data=dict(username='dummy', password='dummy'))
            response = test_client.get(route)
            assert response.status_code == expected

