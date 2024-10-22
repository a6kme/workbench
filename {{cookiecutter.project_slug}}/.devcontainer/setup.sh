#!/bin/bash

# install python dependencies
pip install --upgrade pip
pip install -r api/requirements.txt

sudo apt update

# install postgresql client to access dbshell or psql command
sudo apt install -y postgresql-client

git init

# set git config
git config --global user.email {{cookiecutter.git_email}}
git config --global user.name {{cookiecutter.git_username}}
git config --global --add safe.directory /workspaces/notebooks

# setup node
source $NVM_DIR/nvm.sh
nvm install 20