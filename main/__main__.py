"""
Main application module.
"""
from data_producers.applicant import create_applicant
from data_producers.application import create_application
from data_producers.user import create_admin_login, create_user
from config import CREATE_APPLICANT, CREATE_APPLICATION, CREATE_USER
from utils import get_header
def main():
    """
    Executes methods that are set to True in config.py.
    """
    create_admin_login()
    if CREATE_APPLICANT is True:
        create_applicant()
    if CREATE_APPLICATION is True:
        create_application()
    if CREATE_USER is True:
        create_user()

if __name__ == '__main__':
    main()
