#!/bin/bash

# install python dependencies
pip install --upgrade pip
pip install -r api/requirements.txt

git init

# set git config
git config --global user.email {{cookiecutter.git_email}}
git config --global user.name {{cookiecutter.git_username}}
git config --global --add safe.directory /workspaces/notebooks