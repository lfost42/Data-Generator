"""
Configuration variables for each data generator.
"""
USERS_ENDPOINT = "http://localhost:8080/api/users"
USER_REGISTRATION_ENDPOINT = "http://localhost:8080/api/users/registration"
LOGIN_ENDPOINT = "http://localhost:8080/api/login"
APPLICANTS_ENDPOINT = "http://localhost:8080/api/applicants"
APPLICATIONS_ENDPOINT = "http://localhost:8080/api/applications"

"""
CREATE_APPLICANT: creates a single applicant
"""
CREATE_APPLICANT = False

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
