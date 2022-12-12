'''
Tests user producer methods. 
'''
from data_producers.user import create_admin_login
import pytest

def test_create_admin_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN valid data is passed
    THEN check that the request returns no errors
    """
    assert create_admin_login() == 201

def test_create_admin_not_successful():
    """
    GIVEN static admin data to create an admin account
    WHEN the username is a duplicate (attempts to create the same account twice)
    THEN check that the request returns no errors
    """
    assert create_admin_login() != 201
