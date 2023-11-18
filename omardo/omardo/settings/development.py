from .base import *

SECRET_KEY = "django-secret-key"

DEBUG = True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"
