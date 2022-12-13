'''
Unit tests for utils.py methods.
'''
from program.utils import random_num, get_header

def test_random_num_generator_number():
    """
    GIVEN a number
    WHEN a positive integer is passed in
    THEN check that it returns a number of the correct length
    """
    result_num = random_num(3)
    assert isinstance(result_num, int)
    assert len(str(result_num)) == 3

def test_get_header_successful():
    """
    GIVEN a user admin
    WHEN a valid username and password
    THEN check that it returns successful status code.
    """
    result = get_header()
    assert isinstance(result, dict)
