"""
Submits application requests through the underwriter
microservice endpoint.
"""
import requests
from program.data_producers.applicant import get_applicants
from program.logging_handler import logger
from program.config import APPLICATIONS_ENDPOINT
from program.utils import get_header

def create_applications():
    """Creates applicants via IDs retrieved from the get_applicants method.

    Returns:
        dict: membershipId and socialSecurity for each application created.
    """
    url = APPLICATIONS_ENDPOINT
    applicant_ids = get_applicants()

    data = {
        "applicationType": "SAVINGS",
        "noNewApplicants": True,
        "applicantIds": applicant_ids,
        "applicants": [],
        "applicationAmount": 10000,
        "cardOfferId": 1,
        "depositAccountNumber": "12345"
    }
    header = get_header()
    response = requests.post(url, json = data, headers=header, timeout=1000)

    if response.status_code == 201:
        id_list = [r['membershipId'] for r in response.json()['createdMembers']]
        ssn = [r['socialSecurity'] for r in response.json()['applicants']]
        data_dict = dict(zip(id_list, ssn))

        logger.info("SUCCESS: Created applications")
        return data_dict
    logger.error("No new members created.")
    return {}
