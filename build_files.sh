#!/bin/bash

set -e
set -x

echo "Building project packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Build script completed successfully"