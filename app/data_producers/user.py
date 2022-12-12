"""
Produces random data for users through the user microservice endpoints.
"""
import requests
from ...config import USER_REGISTRATION_ENDPOINT, ADMIN_USERNAME, \
    ADMIN_PASSWORD, ADMIN_EMAIL, ADMIN_PHONE
from ..utils import random_user_id
from ..logging_handler import logger


def create_admin_login():
    """Creates an administrator login account to provide access to
    the applications endpoint in the underwriter microservice.

    Returns:
        json: a response object.
    """
    url = USER_REGISTRATION_ENDPOINT
    user = random_user_id()
    first_name = user[0]
    last_name = user[2]
    admin_data = {
        "username" : ADMIN_USERNAME,
        "password" : ADMIN_PASSWORD,
        "role" : "admin",
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : ADMIN_EMAIL,
        "phone" : ADMIN_PHONE
    }
    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head, timeout=1000)

    if response.status_code == 201:
        logger.info("SUCCESS: Created admin user")
        return response
    logger.error("Admin not created.")
    return response.status_code
