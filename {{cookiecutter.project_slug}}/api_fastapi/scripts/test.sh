#!/usr/bin/env bash

set -e
set -x

export ENVIRONMENT="test"

coverage run --source=api -m pytest
coverage report --show-missing
coverage html --title "${@-coverage}"