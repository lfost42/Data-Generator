"""
Produces random data for users through the user microservice endpoints.
"""
import requests
from program.config import USER_REGISTRATION_ENDPOINT, ADMIN_USERNAME, \
    ADMIN_PASSWORD, ADMIN_PHONE, RANDOM_USERNAME
from program.utils import random_user_id, random_num
from program.logging_handler import logger


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

    if RANDOM_USERNAME is True:
        username = f"{ADMIN_USERNAME}{random_num(4)}"
    else:
        username = ADMIN_USERNAME

    email = f"{username}@smoothstack.com"

    admin_data = {
        "username" : username,
        "password" : ADMIN_PASSWORD,
        "role" : "admin",
        "firstName" : first_name,
        "lastName" : last_name,
        "email" : email,
        "phone" : ADMIN_PHONE
    }
    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head, timeout=1000)

    if response.status_code == 201:
        logger.info("SUCCESS: Created admin user")
        return response.status_code
    #happens rarely when a duplicate email or username is attempted
    logger.error("Admin not created.")
    return response.status_code
