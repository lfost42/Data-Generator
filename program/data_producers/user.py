"""
Produces random data for users through the user microservice endpoints.
"""
import requests
from program.config import USER_REGISTRATION_ENDPOINT, ADMIN_USERNAME, \
    ADMIN_PASSWORD, ADMIN_PHONE, USERS_ENDPOINT
from program.utils import random_user_id, get_header
from program.logging_handler import logger


def create_admin_login():
    """Creates an administrator login account to provide access to
    the applications endpoint in the underwriter microservice.

    Returns:
        When the database does not contain a user:
        json: a response object if successful or a value error if not.
        When the database contains a user, a message is returned
        that a new admin is not needed.
    """
    if get_users():
        logger.info("Only one admin authentication header needed per database")
        raise ValueError("New admin not needed. Will use existing authentication header.")

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
        "email" : f"{ADMIN_USERNAME}@smoothstack.com",
        "phone" : ADMIN_PHONE
    }
    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head, timeout=1000)

    if response.status_code == 201:
        logger.info("SUCCESS: Created admin user")
    # Happens when username or email is not unique, should never happen
    if response.status_code == 409:
        logger.error("Indistinct data, try again.")
        raise ValueError("409: The applicant data conflicts with other data.")

def get_users():
    """Runs a get request to the users endpoint and returns
    email addresses for each applicant found.

    Returns:
        string: List of email addresses for each applicant found.
    """
    url = USERS_ENDPOINT
    header = get_header()
    response = requests.get(url, headers=header, timeout=1000)

    if response.status_code == 200:
        id_list = [r['id'] for r in response.json()['content']]
        logger.info("applicant IDs: " + str(id_list))
        return id_list
    logger.error("Could not get users")
    return response.status_code
