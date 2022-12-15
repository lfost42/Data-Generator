"""Produces random data for users through the user microservice endpoints."""
import requests
# from program.data_producers.application import create_applications
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
        logger.info("ADMIN NOT CREATED: \
            \n Only one admin authentication header needed per database!")
        return {}

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
        return response.json()
    # Happens when username or email is not unique, should never happen
    if response.status_code == 409:
        logger.error("Indistinct data, try again.")
        raise ValueError("409: The applicant data conflicts with other data.")
    return {}

def get_users():
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
            logger.info("applicant IDs: " + str(id_list))
            return id_list
        logger.error("Could not get users")

    except ValueError:
        logger.error("Header not found in get_users.")

    return [] #empty list returned if no users found

# def create_users():
#     pass

# def create_applications():
#     """Creates applicants via IDs retrieved from the get_applicants method.

#     Returns:
#         response: a json reaponse object.
#     """
#     url = USERS_ENDPOINT
#     user_info = create_applications()
#     username = ""
#     password = ""
#     membership_id = ""
#     four_ssn = ""

#     data = {
#         "username": username,
#         "password": password,
#         "role": "MEMBER",
#         "membershipId": membership_id,
#         "lastFourOfSSN": four_ssn
#     }
#     header = get_header()
#     response = requests.post(url, json = data, headers=header, timeout=1000)

#     if response.status_code == 201:
#         logger.info("SUCCESS: Created member users")
#         return response.json()
#     logger.error(response.status_code)
#     return response.status_code
