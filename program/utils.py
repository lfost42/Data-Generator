"""Helper methods."""
import random
import requests
import string
import json
from faker import Faker
from program.logging_handler import logger
from program.config import LOGIN_ENDPOINT

fake = Faker()

def random_num(num: int) -> int:
    """A random number generator that passes in the number of digits as a parameter.

    Args:
        n (int): number of digits for the number needed.

    Returns:
        int: A random number with the required number of digits.
    """
    return random.randint(10 ** (num - 1), 10 ** num - 1)

def random_user_id():
    """A random name generator for first, middle, and last names. Interpolates
    email address using first name, middle initial, and last name.
    Requires unique smail, SSN, DL, and phone#

    Returns:
        string: Random first, middle, last names with email address.
    """
    first_name = fake.first_name()
    middle_name = fake.first_name()
    last_name = fake.last_name()
    email = f"{last_name.lower()}.{first_name.lower()}_{random_num(3)}@email.com"
    return first_name, middle_name, last_name, email


def random_user_info():
    """Generates random user information for Social security number,
    drivers license, phone number, income, and street address.

    Returns:
        string: Social security number, drivers license, phone
        number, income, and street address.
    """
    social_security = fake.ssn()
    drivers_license = f"{random_num(7)}"
    phone_number = f"{random_num(3)} {random_num(3)} {random_num(4)}"
    income = random_num(6)
    address = fake.street_address()
    return social_security, drivers_license, phone_number, income, address

def get_header():
    """Retrieves the authorization header when the admin_login
    user login data is passed to the login endpoint in the user microservice.

    Returns:
        string: An authorization header from the admin_login user.
    """
    url = LOGIN_ENDPOINT
    
    with open('logindata.json', 'r') as f:
        login = json.load(f)

    data = {
        "username" : login['admin']['username'],
        "password" : login['admin']['password']
    }
    response = requests.post(url, json=data, timeout=1000)

    if response.status_code == 200:
        logger.info("Authorization header captured.")
        return {"Authorization" : response.headers["Authorization"]}
    logger.error("Header not saved")
    raise ValueError("Cannot locate a matching header.")

def random_username():
    """A random username using the last_name property of the faker library
    and a 4 digit number appended to avoid data collisions.

    Returns:
        str: a random username.
    """
    return f"{fake.last_name()}_{random_num(5)}"

def random_password():
    """A random password using the random library.

    Returns:
        str: an 8 character password with uppercase, lowercase,
        number, and special characters.
    """
    char = ''.join([random.choice(string.ascii_lowercase) for n in range(4)]).title()
    num = ''.join([random.choice(string.digits) for n in range(3)])
    return char + num + "!"

def admin_login_json():
    """Creates a random username and password, then saves it to
    a json file.

    Returns:
        list: Username and password.
    """
    username = random_username()
    password = random_password()  
    login = {}
    login['admin'] = {'username': username, 'password': password}

    with open('logindata.json', 'w') as f:
        json.dump(login, f)
    logger.info("logindata.json populated:")

    logger.info(login['admin']['username'])
    logger.info(login['admin']['password'])
    return [username, password]
