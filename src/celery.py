from celery import Celery

import src.conf as settings

celery = Celery('app', broker=settings.CELERY_BROKER, backend=settings.CELERY_BACKEND)
celery.conf.beat_schedule = settings.CELERYBEAT_SCHEDULE
celery.autodiscover_tasks(settings.INSTALLED_APPS)