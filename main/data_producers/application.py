"""
Submits application requests through the underwriter
microservice endpoint.
"""
import requests
from logging_handler import logger
from config import APPLICATIONS_ENDPOINT
from utils import get_header
from data_producers.applicant import create_applicant

def create_application():
    """Creates an application from the last ID retrieved from the
    get_applicants method.

    Returns:
        list: membershipId and ssn for the applicant created in a list.
    """
    url = APPLICATIONS_ENDPOINT
    app_id = create_applicant()

    data = {
        "applicationType": "SAVINGS",
        "noNewApplicants": True,
        "applicantIds": app_id,
        "applicants": [],
        "applicationAmount": 10000,
        "cardOfferId": 1,
        "depositAccountNumber": "12345"
    }
    header = get_header()
    response = requests.post(url, json = data, headers=header, timeout=1000)

    if response.status_code == 201:
        # logger.critical(response.json())
        mem_id = response.json()['createdMembers'][0]['membershipId']
        last_four = response.json()['applicants'][0]['socialSecurity'][-4:]
        data_list = [mem_id, last_four]
        logger.info("SUCCESS: Created application")
        # logger.critical(data_list)
        return data_list

    logger.error("No new applications created.")
    return []
