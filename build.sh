#!/usr/bin/env bash
# Exit on error
set -o errexit

# Change to the outer 'todo' directory (where manage.py is located)


# Ensure the Python path includes the outer 'todo' directory


# Install dependencies using Pipenv
pipenv install --deploy --ignore-pipfile

# Collect static files (if needed)


# Apply database migrations
pipenv run python manage.py migrate

# Create a superuser if environment variables are set
if [[ $CREATE_SUPERUSER ]]; then
  pipenv run python manage.py createsuperuser \
    --no-input \
    --email "$DJANGO_SUPERUSER_EMAIL" \
    --username "$DJANGO_SUPERUSER_USERNAME"
fi
