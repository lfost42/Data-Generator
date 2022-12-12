"""
Configuration variables for each data generator.
"""
USER_REGISTRATION_ENDPOINT = "http://localhost:8070/users/registration"
LOGIN_ENDPOINT = "http://localhost:8070/login"
APPLICANTS_ENDPOINT = "http://localhost:8071/applicants"
GET_USERS_ENDPOINT = "http://localhost:8070/users"

"""
Create Admin Variables. Create an admin user if one does not exist.
Required to run create_applicant method.
"""
CREATE_ADMIN = True
ADMIN_USERNAME = "administrator"
ADMIN_PASSWORD = "P@ssword1"
ADMIN_EMAIL = "admin.login@smoothstack.com"
ADMIN_PHONE = "555 555 5555"

"""
Create Applicant variables. Set number of applicants to create.
get_applicants checks whether applicants were populated in the database.
"""
CREATE_APPLICANT = True
NUM_APPLICANTS = 1

GET_APPLICANTS = False
