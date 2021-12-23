python -m venv virenv - create virtual environment

virenv\Scripts\activate.bat - start virtual environment

django-admin start project projectname

python manage.py runserver <port number>

python manage.py startapp playground

INSIDE APP FOLDER
-----------------
admin.py - where we define how the admin interface looks like
apps.py - configure the apps
models.py - where we define models class of the apps
tests.py - where we do unit tests
views.py - where we define the view functions.
A view function takes a request and create a response. It can be called as a request handler.

DEBUG TOOLBAR 
-------------

python -m pip install django-debug-toolbar - install debug toolbar package

Add "debug_toolbar" to your INSTALLED_APPS setting

MIGRATIONS
----------
python manage.py makemigrations - create migrations

python manage.py migrate - apply migrations
 
python manage.py sqlmigrate <appname> <indexofmigrationfile> - check the real sql queries used in a migration

python manage.py migrate <appname> <indexofmigrationfile>

DATABASE
--------
pip install mysqlclient

INSIDE MYSQL WORKBENCH : create database <databasename>

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_name',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'DB_user',
            'PASSWORD': 'DB_password',
        }
    }

#then make migrations 

SET MYSQL PATH 
--------------
set path=%PATH%;C:\Program Files\MySQL\MySQL Server 8.0\bin;

CONNECT
-------
mysql -u root -package

CREATE EMPTY MIGRATION 
----------------------
python manage.py makemigrations store --empty

RUN A SQL QUERY IN A EMPTY MIGRATION FILE 
-----------------------------------------
operations = [
        migrations.RunSQL("""
            INSERT INTO STORE_COLLECTION (title)
            values ("mycollection")
        ""","""
            DELETE FROM STORE_COLLECTION WHERE title = "mycollection"
        """)
    ]

DJANGO ORMS
-----------
query_set = Product.objects.all() - returns queryset
get(pk = 1) - returns object with primary key value 1, throws exception if pk value not found
filter(pk = 1) - returns a query set after filtering the query set and returns a matching object
filter(pk = 1).first() - returns the first row of the queryset
filter(pk = 0).exists() - returns a boolean value depending on the existence of the queryset
filter(unit_price__gt=20) - returns a queryset of values greater than 20
filter(unit_price__gte=20) - greater than equal to
filter(unit_price__lt=20) - less than
filter(unit_price__lte=20) - less than equal to

from django.db.models import Q,F
Q object - to add multiple conditions. eg. filter(Q(unit_price__lt = 10) | Q(inventory__lt = 20))
F object - to compare among different field of same or different table



