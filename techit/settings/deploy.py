from .base import *


def read_secrt(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u2y_$t!rpe3k)flgpi--q!!5e75l751xoctt!8g$@a2%tdyl=+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": read_secrt("MARIADB_DATABASE"),
        "USER": read_secrt("MARIADB_USER"),
        "PASSWORD": read_secrt("MARIADB_PASSWORD"),
        "HOST": "mariadb",
        "PORT": "3306",
    }
}
