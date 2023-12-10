# Django To-Do List App

A simple web-based To-Do List application built using Django and Django Rest Framework.

## Table of Contents

## Features
- Create, Read, Update, and Delete To-Do Items: Perform basic CRUD operations for managing tasks.
- CREATE a To-Do item: /api/todos/ (POST)
- READ one To-Do item: /api/todos/{id}/ (GET)
- READ all To-Do items: /api/todos/ (GET)
- UPDATE a To-Do item: /api/todos/{id}/ (PUT/PATCH)
- DELETE a To-Do item: /api/todos/{id}/ (DELETE)
- Support for Basic Authentication: All APIs are protected with Basic Authentication



## Installation

## Create a virtual environment and activate it:
- python3 -m venv venv
- source venv/bin/activate  # On Linux/Mac
- .\venv\Scripts\activate   # On Windows

## Clone the repository:
- git clone https://github.com/kksain/ToDoList.git

## Navigate to the project directory:
- cd todo_list
  
## Install dependencies:
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Usage

## Run the development server:
python manage.py runserver

## Access the app at http://127.0.0.1:8000/

## API Endpoints:

## Create a To-Do item:
- Endpoint: /api/todos/
- Method: POST
- 
## Read one To-Do item:
- Endpoint: /api/todos/{id}/
- Method: GET
- 
## Read all To-Do items:
- Endpoint: /api/todos/
- Method: GET
- 
## Update a To-Do item:
- Endpoint: /api/todos/{id}/
- Method: PUT/PATCH
- 
## Delete a To-Do item:
- Endpoint: /api/todos/{id}/
- Method: DELETE

## Testing
- Run unit and integration tests:
- python manage.py test

## Postman Collection
- Explore and test API endpoints using the provided Postman Collection:
- ToDoListApp.postman_collection.json

## Authentication
- Basic Authentication is required for API access.

## Features
- Create, read, update, and delete To-Do items
- Assign a title, description, due date, tags, and status to each task
- Django Admin interface for easy management
- RESTful API endpoints for seamless integration
- Basic Authentication for API access
- Unit and integration tests with 100% coverage
