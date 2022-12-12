"""
Main application module.
"""
from main.data_producers.applicant import create_applicant, get_applicants
from main.data_producers.user import create_admin_login
import config


def main():
    """
    Executes methods that are set to True in config.py.
    """
    if config.create_admin is True:
        create_admin_login()
    if config.create_applicant is True:
        create_applicant(config.num_applicants)
    if config.get_applicants is True:
        get_applicants()


if __name__ == '__main__':
    main()
