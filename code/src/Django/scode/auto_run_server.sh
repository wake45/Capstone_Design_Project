#!/bin/bash

python manage.py runserver 0:8000 2>> error.log >> log.log &
