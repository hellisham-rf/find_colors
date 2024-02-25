
==============================
Color Fastapi Project Documentation
==============================

Introduction
============

This project is a simple FastAPI app that It takes a text from you and finds the colors inside the text for you

Installation
============

To install and run this project, you will need the following:

- Python 3.8 or later
- Django 5.0 or later
- fastapi[all]

You can install the required Python packages using pip
::

    pip install -r requirements.txt


To start the development server, you can run
::
     uvicorn main:app --reload



You can then access the application at http://localhost:8000.


URLS
-----------

    - **/color**: It takes a text from you and finds the colors inside the text for you
    - **/docs** : This is a documentation of this app.