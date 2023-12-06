# Django To-Do List App

A simple web-based To-Do List application built using Django and Django Rest Framework.

## Table of Contents

Features
Create, Read, Update, and Delete To-Do Items: Perform basic CRUD operations for managing tasks.

Task Attributes:

Timestamp: Automatically set on task creation and not editable by users.
Title: User-settable with a maximum length of 100 characters (mandatory field).
Description: User-settable with a maximum length of 1000 characters (mandatory field).
Due Date: User-settable while creating or updating a task (optional field).
Tag: One or more tags can be added to a task. Tags are user-settable and can be changed.
Status: Indicates the status of a task and can be one of the following:
OPEN (Default)
WORKING
DONE
OVERDUE (optional field)
Django Admin Interface:

Enforces validation checks on attributes.
Changelist view with filters for each model.
Proper fieldsets for each model.
REST APIs using Django Rest Framework (DRF):

CREATE a To-Do item: /api/todos/ (POST)
READ one To-Do item: /api/todos/{id}/ (GET)
READ all To-Do items: /api/todos/ (GET)
UPDATE a To-Do item: /api/todos/{id}/ (PUT/PATCH)
DELETE a To-Do item: /api/todos/{id}/ (DELETE)
Postman Collection: Shareable collection for testing API endpoints.

Support for Basic Authentication: All APIs are protected with Basic Authentication.

Tests:

Unit Tests: Covering individual components and functions.
Integration Tests: Covering the interaction between different components.
Code Coverage: Aim for 100% code coverage.
Continuous Integration (GitHub Actions):

Run Tests Automatically: Unit tests and integration tests on every push.
Linting Tools: Check code formatting using Flake8 and Black.

## Installation
Clone the repository:
git clone https://github.com/kksain/ToDoList.git

## Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
.\venv\Scripts\activate   # On Windows
## Install dependencies:
pip install -r requirements.txt
## Apply migrations:
python manage.py migrate
## Usage
Run the development server:
python manage.py runserver
Access the app at http://127.0.0.1:8000/

### API Endpoints

## Create a To-Do item:
Endpoint: /api/todos/
Method: POST
## Read one To-Do item:
Endpoint: /api/todos/{id}/
Method: GET
## Read all To-Do items:
Endpoint: /api/todos/
Method: GET
## Update a To-Do item:
Endpoint: /api/todos/{id}/
Method: PUT/PATCH
## Delete a To-Do item:
Endpoint: /api/todos/{id}/
Method: DELETE

## Testing
Run unit and integration tests:
python manage.py test

## Postman Collection
Explore and test API endpoints using the provided Postman Collection:
ToDoListApp.postman_collection.json

## Authentication
Basic Authentication is required for API access.

## Features

- Create, read, update, and delete To-Do items
- Assign a title, description, due date, tags, and status to each task
- Django Admin interface for easy management
- RESTful API endpoints for seamless integration
- Basic Authentication for API access
- Unit and integration tests with 100% coverage
