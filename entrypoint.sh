#!/bin/sh

export DJANGO_SETTINGS_MODULE=omardo.settings.production

echo 'Running collecstatic...'
python omardo/manage.py collectstatic --no-input

echo 'Applying migrations...'
python omardo/manage.py migrate

echo 'Running server...'
python omardo/manage.py runserver 0.0.0.0:8000

#gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:$PORT