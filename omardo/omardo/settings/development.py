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

DEVELOPMENT_APPS = [
    "django_browser_reload",
]

DEVELOPMENT_MIDDLEWARE = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

INSTALLED_APPS = INSTALLED_APPS + DEVELOPMENT_APPS

MIDDLEWARE = MIDDLEWARE + DEVELOPMENT_MIDDLEWARE

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"
