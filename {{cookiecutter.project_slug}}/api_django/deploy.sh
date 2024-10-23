#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn -k uvicorn.workers.UvicornWorker api.asgi:application