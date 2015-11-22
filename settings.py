# coding: utf-8


"""App settings"""

import os


# Mongo settings
MONGODB_SETTINGS = {
    "HOST": os.environ.get("MONGOLAB_URI", None),
    "DB": "cbasounds"
}

# App secret
SECRET_KEY = "2po89gvuhpfvnhp98r5phnf"

# Mail settings
MAIL_SERVER = 'pop.faudi.unc.edu.ar'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USERNAME = 'youremail@institution.edu'
MAIL_PASSWORD = 'changeme'

# Security settings
SECURITY_EMAIL_SENDER = 'youremail@institution.edu'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'your salt'
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
