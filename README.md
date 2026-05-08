# Task Workflow API

Backend task workflow system built with FastAPI.

## Overview

This project is a backend API designed for managing users and workflow tasks. It provides functionality for task creation, task management, user registration, and API-based workflow operations.

The project was built to strengthen backend development skills using modern Python technologies and REST API principles.

---

## Features

- User registration system
- Task creation and management
- RESTful API endpoints
- FastAPI backend framework
- SQLite database integration
- Pydantic schema validation
- Environment variable support with `.env`
- Interactive API documentation with Swagger UI

---

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/israelolutobi/task-workflow-api.git
```

Navigate into the project directory:

```bash
cd task-workflow-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

---

## API Documentation

FastAPI automatically generates interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Future Improvements

- JWT authentication
- Task filtering and querying
- Role-based permissions
- PostgreSQL integration
- Docker deployment
- Unit testing

---

## Project Status

Active development
