"""
Main application module.
"""
import logging
from app.data_producers.applicant import create_applicant, get_applicants
from app.data_producers.user import create_admin_login
from .config import CREATE_ADMIN, CREATE_APPLICANT, \
    GET_APPLICANTS, NUM_APPLICANTS


def main():
    """
    Executes methods that are set to True in config.py.
    """
    if CREATE_ADMIN is True:
        create_admin_login()
    if create_applicant is True:
        create_applicant(NUM_APPLICANTS)
    if get_applicants is True:
        get_applicants()
    if False in (CREATE_ADMIN, CREATE_APPLICANT, GET_APPLICANTS):
        logging.warning('Not all available methods were executed. \
            \nPlease modify config.py to run additional methods.')


if __name__ == '__main__':
    main()
