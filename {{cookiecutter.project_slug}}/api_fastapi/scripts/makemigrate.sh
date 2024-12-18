#!/usr/bin/env bash

set -e  # Exit immediately if a command exits with a non-zero status
set -x  # Print commands and their arguments as they are executed

# Set PYTHONPATH to the parent directory of the script's location
export PYTHONPATH="$(dirname "$(dirname "$(dirname "$(realpath "$0")")")")"

# Define color codes
RED='\033[0;31m'
NC='\033[0m' # No Color

# Prompt for the name of the migration
read -p "Enter the migration name (minimum 5 characters): " migration_name

# Check if the migration name is empty or less than 5 characters
{%- raw %}
if [[ -z "$migration_name" || ${#migration_name} -lt 5 ]]; then
  echo -e "${RED}Error: Migration name must be at least 5 characters long.${NC}"
  exit 1
fi
{%- endraw %}

# Generate the Alembic revision with the provided migration name
alembic -c api/alembic.ini revision --autogenerate -m "$migration_name"
