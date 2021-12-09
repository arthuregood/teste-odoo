#!/bin/sh
apt update
apt install python3-dev python3-pip libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev postgresql postgresql-contrib python-passlib -y
pip3 install vatnumber
pip3 install pipenv
apt update && apt upgrade -y
