"""
Configuration variables for each data generator. The default
endpoints do not utilize aline-gateway.
"""
USER_REGISTRATION_ENDPOINT = "http://localhost:8070/users/registration"
LOGIN_ENDPOINT = "http://localhost:8070/login"
APPLICANTS_ENDPOINT = "http://localhost:8071/applicants"
GET_USERS_ENDPOINT = "http://localhost:8070/users"

"""
Set CREATE_ADMIN to True if running scripts on a new database or to
create a new admin login user account. Required to execute CREATE_APPLICANT.
Set RANDOM_USERNAME to False to create a static admin user account. 
"""
CREATE_ADMIN = True
ADMIN_USERNAME = "administrator_1" #increment when running a new test
RANDOM_USERNAME = False #set to false for testing
ADMIN_PASSWORD = "P@ssword1"
ADMIN_EMAIL = "admin.login@smoothstack.com"
ADMIN_PHONE = "555 555 5555"

"""
CREATE_APPLICANT: set number of applicants desired. Default is 1.
GET_APPLICANTS: check whether applicants were populated in the database.
Default is False.
"""
CREATE_APPLICANT = True
NUM_APPLICANTS = 1

GET_APPLICANTS = False
