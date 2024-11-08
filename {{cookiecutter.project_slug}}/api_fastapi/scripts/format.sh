#!/bin/sh -e
set -x

ruff check api api/scripts --fix
ruff format api api/scripts
