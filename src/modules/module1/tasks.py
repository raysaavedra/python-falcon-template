from src.celery import celery

@celery.task()
def ping():
    print('pong')