#!/bin/bash

mkdir -p staticfiles static

echo "Connecting to PostgreSQL at db:5432"

# Database check
echo "Waiting for PostgreSQL..."
while ! nc -z "db" "5432"; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done
echo "PostgreSQL started"

# Run migrations
echo "Running migrations"
python manage.py migrate

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --no-input

# Start Django server
echo "Starting Django server"
exec gunicorn --bind 0.0.0.0:8000 core.wsgi --workers=4 --threads=2 --timeout=120
