# python-falcon-template
A sample template for Python Falcon API application. This also provides a sample on how to implement celery in Falcon.

## Install
```
pip install -r requirements/base.txt
```

## Folders
* requirements
    - includes all dependencies for the project
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