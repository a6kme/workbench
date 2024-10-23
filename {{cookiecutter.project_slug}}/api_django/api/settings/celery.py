import os

CELERY_BROKER_URL = os.environ.get('RABBITMQ_URL')
