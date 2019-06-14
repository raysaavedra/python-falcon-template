import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SERVER
HOST='0.0.0.0'
PORT=8001

SECRET_KEY='secret'

ALLOWED_HOSTS = [
    '*'
]

#List of all modules use in the app.
#Primarily used by celery to find all tasks.
INSTALLED_APPS = [
    'src.modules.module1'
]

# CELERY
CELERY_BROKER='redis://localhost:5103/0'
CELERY_BACKEND='redis://localhost:5103/0'

CELERYBEAT_SCHEDULE = {
    'test-celery-sched': {
        'task': 'src.modules.module1.tasks.ping',
        'schedule': 10.0,
    },
}

try:
    from .local_settings import *
except ImportError:
    pass