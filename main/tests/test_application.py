"""Tests for application generator method."""
from main.data_producers.application import create_application

def test_create_application_returns_list():
    """
    GIVEN a bearer token
    WHEN the proper http get is requested
    THEN check that it returns a list that is not empty.
    """
    result = create_application()
    assert isinstance(result, list)
    assert create_application()
