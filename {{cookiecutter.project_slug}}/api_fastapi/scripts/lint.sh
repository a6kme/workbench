#!/usr/bin/env bash

set -e
set -x

mypy app

# Check if the argument --fix is passed
if [[ "$1" == "--fix" ]]; then
    ruff check app --fix
    ruff format app
else
    ruff check app
    ruff format app --check
fi

