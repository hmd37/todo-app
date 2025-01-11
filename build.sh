#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies using Pipenv
pipenv install --deploy --ignore-pipfile

# Activate Pipenv environment
pipenv run python manage.py collectstatic --no-input
pipenv run python manage.py migrate

# Create superuser if environment variables are set
if [[ $CREATE_SUPERUSER ]]; then
  pipenv run python manage.py createsuperuser --no-input --email "$DJANGO_SUPERUSER_EMAIL"
fi
