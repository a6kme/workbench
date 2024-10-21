#!/bin/bash

# install python dependencies
pip install --upgrade pip
pip install -r api/requirements.txt

sudo apt update

{% if cookiecutter.use_database == 'yes' and cookiecutter.database == 'postgresql' -%}
sudo apt install -y postgresql-client
{%- endif %}

git init

# set git config
git config --global user.email {{cookiecutter.git_email}}
git config --global user.name {{cookiecutter.git_username}}
git config --global --add safe.directory /workspaces/notebooks

# setup node
nvm install 20