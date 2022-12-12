"""
Produces random data for users through the user microservice endpoints.
"""
import requests
import config
from main.utils import random_user_id
from main.logging_handler import logger


def create_admin_login():
    """Creates an administrator login account to provide access to
    the applications endpoint in the underwriter microservice.

    Returns:
        json: a response object.
    """
    url = config.user_registration_endpoint
    user = random_user_id()
    first_name = user[0]
    last_name = user[2]
    admin_data = {
        "username" : config.admin_username,
        "password" : config.admin_password,
        "role" : "admin",
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : config.admin_email,
        "phone" : config.admin_phone
    }
    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head, timeout=1000)

    if response.status_code == 201:
        logger.debug(f"{response.status_code}: Created admin user")
        return response
    logger.error(f"{response.status_code}: Admin not created.")
    return response.status_code
