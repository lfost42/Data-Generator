"""
Configuration variables for each data generator. The default
endpoints do not utilize aline-gateway.
"""
USERS_ENDPOINT = "http://localhost:8070/users"
USER_REGISTRATION_ENDPOINT = "http://localhost:8070/users/registration"
LOGIN_ENDPOINT = "http://localhost:8070/login"
APPLICANTS_ENDPOINT = "http://localhost:8071/applicants"

"""
Creates a new admin login user account. Required to execute CREATE_APPLICANT.
Will only run when database does not contain a user.
"""
ADMIN_USERNAME = "admin_1"
ADMIN_PASSWORD = "P@ssword1"
ADMIN_PHONE = "555 555 5555"

GET_USERS = True

"""
CREATE_APPLICANT: set number of applicants desired. Default is 1.
GET_APPLICANTS: check whether applicants were populated in the database.
Default is False.
"""
CREATE_APPLICANT = True
NUM_APPLICANTS = 1

GET_APPLICANTS = True
