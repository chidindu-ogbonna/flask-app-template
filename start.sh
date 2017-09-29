#!/bin/bash

mkvirtualenv -p python3 flask-app
workon flask-app
pip install -r requirements.txt
python manage.py runserver
