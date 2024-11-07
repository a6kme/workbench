#! /usr/bin/env bash

# Set PYTHONPATH to the parent directory of the script's location
export PYTHONPATH="$(dirname "$(dirname "$(realpath "$0")")")"

set -e
set -x

# Let the DB start
python app/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python app/initial_data.py
