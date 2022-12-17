"""
Configuration variables for each data generator. The default
endpoints do not utilize aline-gateway.
"""
USERS_ENDPOINT = "http://localhost:8070/users"
# USER_REGISTRATION_ENDPOINT = "http://localhost:8080/api/users/registration"
USER_REGISTRATION_ENDPOINT = "http://localhost:8070/users/registration"
# LOGIN_ENDPOINT = "http://localhost:8080/api/login"
LOGIN_ENDPOINT = "http://localhost:8070/login"
APPLICANTS_ENDPOINT = "http://localhost:8071/applicants"
APPLICATIONS_ENDPOINT = "http://localhost:8071/applications"

"""
CREATE_APPLICANT: creates a single applicant
"""
CREATE_APPLICANT = True

"""
CREATE_APPLICATION: Creates an application for a saving account for
the last each applicant created. Default is False because it is
invoked when CREATE_USER is called.
"""
CREATE_APPLICATION = False

"""
CREATE_USER: takes a invokes CREATE_APPLICATION to create a member user.
"""
CREATE_USER = True
