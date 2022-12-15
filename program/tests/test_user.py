"""Tests for user generator methods."""
from program.data_producers.user import create_admin_login, get_user_ids#, create_users


def test_create_admin_login_returns_empty_dict():
    """
    GIVEN a valid bearer token
    WHEN a valid admin authentication is stored in the database
    THEN check that it returns an empty dictionary.
    """
    result = create_admin_login()
    assert isinstance(result, dict)
    assert len(result) == 0

def test_get_user_ids_returns_list():
    """
    GIVEN a valid bearer token
    WHEN the proper http GET is requested
    THEN check that it returns a list that is not empty.
    """
    result = get_user_ids()
    assert isinstance(result, list)
    assert get_user_ids()

# def test_create_users_returns_dict():
#     """
#     GIVEN a bearer token
#     WHEN the proper http get is requested
#     THEN check that it returns a dictionary that is not empty.
#     """
#     result = create_users()
#     assert isinstance(result, dict)
#     assert create_users()
