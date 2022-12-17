"""Produces random data for users through the user microservice endpoints."""
import requests
from program.config import USER_REGISTRATION_ENDPOINT, USERS_ENDPOINT
from program.utils import random_user_id, get_header, random_username, \
    random_password, admin_login_json
from program.data_producers.application import create_application
from program.logging_handler import logger

def get_user_ids():
    """Runs a get request to the users endpoint and returns
    email addresses for each applicant found.

    Returns:
        string: List of email addresses for each applicant found
        or an empty list if no users found.
    """
    try:
        header = get_header()
        url = USERS_ENDPOINT
        response = requests.get(url, headers=header, timeout=1000)

        if response.status_code == 200:
            id_list = [r['id'] for r in response.json()['content']]
            logger.info("User IDs: " + str(id_list))
            return id_list
        logger.error("Could not get users")

    except ValueError:
        logger.error("Header not found in get_users.")
    return []

def create_admin_login():
    """Creates an administrator login account to provide access to
    the applications endpoint in the underwriter microservice.

    Returns:
        When the database does not contain a user:
        json: a response object if successful or a value error if not.
        When the database contains a user, a message is returned
        that a new admin is not needed.
    """
    if get_user_ids():
        logger.info("ADMIN NOT CREATED: \
            \n Only one admin authentication header needed per database!")
        return {}

    url = USER_REGISTRATION_ENDPOINT
    user = random_user_id()
    admin = admin_login_json()

    admin_data = {
        "username" : admin[0],
        "password" : admin[1],
        "role" : "admin",
        "firstName" : user[0],
        "lastName" : user[2],
        "email" : f"{admin[0]}@company.com",
        "phone" : "555-555-5555"
    }

    head = {'Content-Type': 'application/json'}
    response = requests.post(url, json=admin_data, headers=head, timeout=1000)

    if response.status_code == 201:
        logger.info("SUCCESS: Created admin user")
        return response.json()
    return {}

def create_user():
    """Creates member user by sending a request to the useres endpoint
    via the user microservice.

    Returns:
        dict: An http response in json format.
    """
    url = USER_REGISTRATION_ENDPOINT
    values = create_application()
    username = random_username()
    password = random_password()

    data = {
        "username": username,
        "password": password,
        "role": "member",
        "membershipId": values[0],
        "lastFourOfSSN": values[1]
    }

    header = get_header()
    response = requests.post(url, json = data, headers=header, timeout=1000)

    if response.status_code == 201:
        logger.info("SUCCESS: Created user with role of member.")
        return response.json()
    logger.critical(response.status_code)
    return {}
