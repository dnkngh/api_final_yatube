# Yatube API
Yatube API is a DRF project that allows you to interract with Yatube functions via API, such as:

- Creating, read, update and delete posts and comments
- Getting a full list of posts on the project
- Getting a list of posts related to a specific group
- Getting a full list of comment on the project
- Getting a list of comments related to a specific post
- Following and unfollowing users

Documentation and request/response examples will be alwailible for you on http://127.0.0.1:8000/redoc/ once you run the server.

## Used technologies
- Python 3.7
- Django 3.2
- Django REST Framework
- JWT + Djoser

## Installation
1. Fork and clone the repository `git clone {ur repository URL}`
2. Set up virtual environment `python -m venv venv`
3. Upgrade pip `python -m pip install --upgrade pip`
4. Activate virtual environment `source /venv/scripts/activate` (Win)
5. Install dependencies: `pip install -r requirements.txt`
6. Apply migrations `python manage.py mirate`
7. Run a development server `python manage.py runserver` 
