import os
from .common import *
import dj_database_url


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['python-django-ecommerce-prod-ff911dd41727.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = 'MAILGUN_SMTP_LOGIN'
EMAIL_HOST_PASSWORD = 'MAILGUN_SMTP_PASSWORD'
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']