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
    admin_name = f"{ADMIN_USERNAME}{random_num(3)}"
    email = f"{admin_name}@smoothstack.com"

    admin_data = {
        "username" : admin_name,
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
    # Happens when username or email is not unique, should almost never happen
    elif response.status_code == 409:
        logger.error("Indistinct data, try again.")
        raise ValueError("409: The applicant data conflicts with other data.")
