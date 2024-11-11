#! /usr/bin/env bash

set -e
set -x

# Set PYTHONPATH to the parent directory of the script's location
export PYTHONPATH="$(dirname "$(dirname "$(dirname "$(realpath "$0")")")")"

# Let the DB start
python api/backend_pre_start.py

# Run migrations
alembic -c api/alembic.ini upgrade head

# Create initial data in DB
# python api/initial_data.py