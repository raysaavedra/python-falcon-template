# python-falcon-template
A sample template for Python Falcon API application. This also provides a sample on how to implement celery in Falcon.

## Install
```
pip install -r requirements/base.txt
```

## Folders
* requirements
    - includes all dependencies for the project
    * base.txt
        - main requirements file
    * dev.txt
        - all your dev requirements
* conf
    - includes the settings file
    - add local_settings.py in conf folder to override any value in settings file
* middleware
    - includes all middleware files
* core
    - includes all necessary files used in the app
    * resource.py
        - includes base resource class
    * routes.py
        - includes main function to register routes
        - file to add all your routes
    * test.py
        - includes base test class
* modules
    - includes all modules in your app
    - per module folder, test folder should be included
* app.py
    - includes create_app function
    - is where you define your middlewares and other settings
* celery.py
    - includes celery declaration
* runserver.sh
    - script to quickly run server
* runtest.sh
    - script to quickly run tests

## How to run server
* make sure runserver.sh is executable
```
./runserver.sh
```

## How to run tests
* make sure runtest.sh is executable
```
./runtest.sh
```

# Celery

## How to run celery
* we are using redis as our celery broker, so make sure to install redis-server
* run redis-server and update CELERY settings found on src/conf/settings.py
* how to run celery:
    ```
    celery -A src.celery.celery worker --loglevel=info
    ```
    ```
    celery -A src.celery.celery beat -l debug
    ```

## How to add tasks in celery
* sample can be found on modules/module1/tasks.py
```python
from src.celery import celery

@celery.task()
def ping():
    print('pong')
```

## How to handle scheduled tasks in celery
* update CELERYBEAT_SCHEDULE found on src/conf/settings.py
```python
CELERYBEAT_SCHEDULE = {
    'test-celery-sched': {
        'task': 'src.modules.module1.tasks.ping',
        'schedule': 10.0,
    },
}
```

