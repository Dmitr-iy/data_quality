#!/usr/bin/bash

sleep 3;
python manage.py migrate

sleep 3;
python manage.py runserver 0.0.0.0:8000