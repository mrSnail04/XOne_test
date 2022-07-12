#!/bin/bash

python url_shorter/manage.py makemigrations --no-input
python url_shorter/manage.py migrate --no-input
python url_shorter/manage.py runserver 0.0.0.0:$PORT
