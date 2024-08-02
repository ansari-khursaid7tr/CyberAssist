#!/usr/bin/env bash

echo "Building project packages..."
python3 -m pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Compressing static files..."
python3 manage.py compress