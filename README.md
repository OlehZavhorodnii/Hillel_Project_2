# Django project

## Directories and files

    manage.py - script for project management
    config/ - project directory
        __init__.py - indicates that the folder it is in will be treated as a module
        settings.py - contains project configuration settings
        urls.py - defines the project's routing system
        wsgi.py - contains WSGI (Web Server Gateway Interface) configuration properties
    core/ - application directory
        migrations/ - stores information that allows you to map the database and model definitions
        __init__.py - tells the python interpreter that the current directory will be treated as a package
        admin.py - intended for administrative functions
        apps.py - defines the configuration of the application
        models.py - stores the definition of models that describe the data used in the application
        tests.py - stores application tests
        views.py - defines functions that receive user requests, process them and return a response
