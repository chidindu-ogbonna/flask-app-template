# Template For A Flask Application

**A complete, and extensible Flask application template, with useful plugins.**

Use this Flask app to initiate your project with less work. In this application  template you will find the following plugins already configured:

* **Flask-Login** - Flask-Login provides user session management for Flask.
* **Flask-Bootstrap** - Ready-to-use Twitter-bootstrap for use in Flask.
* **Flask-Admin** - Flask extension module that provides an admin interface
* **Flask-Mail** - Makes sending mails from Flask applications very easy and has also support for unittesting.
* **pytest** and **pytest-flask** - Unitesting using the pytest framework specifically for flask
* **Flask-SQLAlchemy** - Adds SQLAlchemy support to Flask. Quick and easy.
* **Werkzeug** - The **security** module is used for password hashing.
* **Flask-Admin** - Provides an Admin interface to monitor what is going on in the database.
* **Flask-Migrate** - Version Control for the database models
* **Flask-WTF** - Flask-Themes makes it easy for your application to support a wide range of appearances.

## Requirements

python (any version, preferably 3+), python-pip, virtualenv, virtualenvwrapper

## Instalation

First, clone this repository:

    $ git clone http://github.com/chidonna/flask-app
    $ cd flask-app

Create a virtualenv, and activate it:

    $ mkvirtualenv -p python3 flask-app
    $ workon flask-app

After, install all necessary to run:

    $ pip install -r requirements.txt

To run the tests

    $ py.test

Then, run the application:

	$ python manage.py runserver

To see your application, access this url in your browser:

	http://localhost:5000

## Furthermore

After changes have been made to the "models.py", make sure to run the migrate commands for it to be added to the database

    $ python manage.py db migrate -m '{commit message}'
    $ python manage.py db upgrade


