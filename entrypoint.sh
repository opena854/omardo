#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=config.settings.production

echo 'Applying migrations...'
python omardo/manage.py migrate --settings=config.settings.production


echo 'Running server...'
python omardo/manage.py runserver 0.0.0.0:8000 --settings=config.settings.production

#gunicorn --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:$PORT