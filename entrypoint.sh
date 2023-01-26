#!/bin/sh

set -e

echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting the Django development server on localhost..."
python manage.py runserver 0.0.0.0:8000
