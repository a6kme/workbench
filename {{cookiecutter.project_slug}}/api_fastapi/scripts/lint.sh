#!/usr/bin/env bash

set -e
set -x

mypy api
ruff check api
ruff format api --check