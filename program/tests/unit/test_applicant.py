'''
Tests applicant producer methods.
'''
import json
from program.data_producers.applicant import create_applicant, get_applicants

def test_create_applicant_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN valid data is passed
    THEN check that the request returns no errors
    """
    result = create_applicant(1)
    response_json = json.loads(result.text)
    assert isinstance(response_json, dict)

def test_get_applicants_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN valid data is passed
    THEN check that the request returns no errors
    """
    result = get_applicants()
    response_json = json.loads(result.text)
    assert isinstance(response_json, dict)
