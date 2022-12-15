"""Applicant method tests."""
from program.data_producers.applicant import create_applicant, get_applicants

def test_create_applicant_returns_list():
    """
    GIVEN a bearer token
    WHEN the proper http POST is requested
    THEN check that it returns a dictionary.
    """
    result = create_applicant(1)
    assert isinstance(result, list)

def test_get_applicants_returns_list():
    """
    GIVEN a bearer token
    WHEN the proper http GET is requested
    THEN check that it returns a list.
    """
    result = get_applicants()
    assert isinstance(result, list)
