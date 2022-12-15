"""
Produces random data for applicant through underwriter
microservice endpoints.
"""
import requests
from program.config import APPLICANTS_ENDPOINT
from program.logging_handler import logger
from program.utils import random_user_id, random_user_info, get_header


def create_applicant(num_applicants):
    """Creates the number of applicants specified in config.py.

    Args:
        num_applicants (int): Number of applicants to create.

    Returns:
        string: Response if successful, status code if not.
    """
    url = APPLICANTS_ENDPOINT
    first_name, middle_name, last_name, email = random_user_id()
    social_security, drivers_license, phone_number, income, address = random_user_info()

    for _ in range(num_applicants):
        data = {
            "firstName": first_name,
            "middleName": middle_name,
            "lastName": last_name,
            "dateOfBirth": "1991-07-09",
            "gender": "UNSPECIFIED",
            "email": email,
            "phone": phone_number,
            "socialSecurity": social_security,
            "driversLicense": drivers_license,
            "income": income,
            "address": address,
            "city": "McLean",
            "state": "Virginia",
            "zipcode": "22102",
            "mailingAddress": address,
            "mailingCity": "McLean",
            "mailingState": "Virginia",
            "mailingZipcode": "22102"
        }
        header = get_header()
        response = requests.post(url, json = data, headers=header, timeout=1000)

        if response.status_code == 201:
            logger.info(f"SUCCESS: Created applicant \
                {last_name}, {first_name}")
            return response.json()
        logger.critical(response.status_code)
        return {}

def get_applicants():
    """Runs a get request to the applicants endpoint and returns
    the ID for every applicant found.

    Returns:
        array: Array of applicant IDs.
    """
    url = APPLICANTS_ENDPOINT
    header = get_header()
    response = requests.get(url, headers=header, timeout=1000)

    if response.status_code == 200:
        id_list = [r['id'] for r in response.json()['content']]
        logger.info("applicant IDs: " + str(id_list))
        return id_list

    logger.critical(response.status_code)
    return {}
