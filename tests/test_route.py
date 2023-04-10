import pytest
from . import flask_app


def test_index(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/'
    THEN the status code should be 200"
    """
    response = test_client.get("/")
    assert response.status_code == 200