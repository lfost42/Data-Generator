"""Tests for application generator method."""
from program.data_producers.application import create_applications

def test_get_applicants_returns_list():
    """
    GIVEN a bearer token
    WHEN the proper http get is requested
    THEN check that it returns a dictionary.
    """
    result = create_applications()
    assert isinstance(result, dict)
