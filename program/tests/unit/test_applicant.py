'''
Tests applicant producer methods. 
'''
from program.data_producers.applicant import create_applicant, get_applicants

def create_applicant_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN valid data is passed
    THEN check that the request returns no errors
    """
    assert create_applicant() == 201

def get_applicants_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN valid data is passed
    THEN check that the request returns no errors
    """
    assert get_applicants() == 200