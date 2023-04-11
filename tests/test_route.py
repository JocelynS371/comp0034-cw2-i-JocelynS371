import pytest
import flask_app


import pytest

@pytest.mark.parametrize('route', ['/', '/login', '/register', '/data-entry', '/predict' ])
def test_route_get(test_client, route):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to functional routes
    THEN the status code should be 200"
    """
    response = test_client.get(route)
    assert response.status_code == 200


