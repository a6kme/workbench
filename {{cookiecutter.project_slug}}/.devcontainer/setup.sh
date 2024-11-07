#!/bin/bash

install python dependencies
pip install --upgrade pip
pip install -r api/requirements.txt

sudo apt update

# install postgresql client to access dbshell or psql command
sudo apt install -y postgresql-client

echo "Setting up git config in directory $(pwd)"

# set git config
git config --global init.defaultBranch main
git config --global user.email abhishek@a6k.me
git config --global user.name abhishek
git config --global --add safe.directory "$(pwd)"

git init

# setup node
source $NVM_DIR/nvm.sh
nvm install 20
cd ui && npm install
