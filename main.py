"""
Main application module.
"""
from program.data_producers.applicant import create_applicant, get_applicants
from program.data_producers.user import create_admin_login
from program.config import CREATE_APPLICANT, GET_APPLICANTS, NUM_APPLICANTS, \
    CREATE_APPLICATIONS
from program.data_producers.application import create_applications

def main():
    """
    Executes methods that are set to True in config.py.
    """
    create_admin_login()
    if CREATE_APPLICANT is True:
        create_applicant(NUM_APPLICANTS)
    if GET_APPLICANTS is True:
        get_applicants()
    if CREATE_APPLICATIONS is True:
        create_applications()

if __name__ == '__main__':
    main()
