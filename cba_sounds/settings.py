# coding: utf-8


"""App settings"""

import os


# Server settings
PORT = 5000

# Mongo settings
MONGODB_SETTINGS = {
    "HOST": os.environ.get("MONGOLAB_URI", None),
    "DB": "cbasounds"
}

# App secret
SECRET_KEY = "2po89gvuhpfvnhp98r5phnf"

# Mail settings
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_SSL = False

# Security settings
SECURITY_EMAIL_SENDER = 'youremail@institution.edu'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'your salt'
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
