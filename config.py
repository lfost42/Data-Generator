"""
Configuration variables for each data generator. The default
endpoints do not utilize aline-gateway.
"""
USER_REGISTRATION_ENDPOINT = "http://localhost:8070/users/registration"
LOGIN_ENDPOINT = "http://localhost:8070/login"
APPLICANTS_ENDPOINT = "http://localhost:8071/applicants"
GET_USERS_ENDPOINT = "http://localhost:8070/users"

"""
Creates a new admin login user account. Required to execute CREATE_APPLICANT.
"""
CREATE_ADMIN = True
ADMIN_USERNAME = "admin_"
RANDOM_USERNAME = True
ADMIN_PASSWORD = "P@ssword1"
ADMIN_PHONE = "555 555 5555"

"""
CREATE_APPLICANT: set number of applicants desired. Default is 1.
GET_APPLICANTS: check whether applicants were populated in the database.
Default is False.
"""
CREATE_APPLICANT = True
NUM_APPLICANTS = 1

GET_APPLICANTS = False
