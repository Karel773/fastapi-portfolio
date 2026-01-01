# FastAPI Task Manager 

A simple project for managing users and tasks, built with **FastAPI**, **SQLAlchemy** and **Pydantic**.
This project demonstrates backend development skills and is suitable as a portfolio project for Python developers.

--- 

## Technologies 

- Python 3.14 
- FastAPI 
- SQLAlchemy 
- Pydantic 
- SQLite 
- Uvicorn (ASGI server) 
- Git / GitHub 

--- 

## Installation 

1. Clone the repository: 

```bash 
git clone https://github.com/Karel773/fastapi-portfolio.git 
cd fastapi-portfolio```

2. Create and activate a virtual environment: 

# Windows 
python -m venv venv 
venv\Scripts\activate 

# macOS / Linux 
python -m venv venv 
source venv/bin/activate 

3. Install required packages: 
```bash
pip install -r requirements.txt``` 

4. Run the server: 
```bash 
uvicorn main:app --reload``` 

5. Open the API documentation in your browser: 

http://127.0.0.1:8000/docs

--- 

## Project Structure 

- `main.py`        # Main FastAPI application
- `models.py`      # SQLAlchemy models
- `schemas.py`     # Pydantic schemas
- `database.py`    # Database configuration and session setup
- `routers/`
    - `users.py`   # CRUD operations for users
    - `tasks.py`   # CRUD operations for tasks
- `requirements.txt`
- `README.md`

## API Endpoints

**Users**
- `POST /users` – Create a new user
- `GET /users` – Get all users
- `GET /users/{user_id}` – Get a user by ID
- `PUT /users/{user_id}` – Update a user
- `DELETE /users/{user_id}` – Delete a user

**Tasks**
- `POST /tasks` – Create a new task
- `GET /tasks` – Get all tasks
- `GET /tasks/{task_id}` – Get a task by ID
- `PUT /tasks/{task_id}` – Update a task
- `DELETE /tasks/{task_id}` – Delete a task

---

## Features 

- Full CRUD operations for users and tasks 
- Input validation using Pydantic 
- Automatic database table creation with SQLAlchemy 
- Status codes properly set (201 Created, 204 No Content, 404 Not Found) 
- Endpoints organized with FastAPI routers 
- Swagger UI documentation available at /docs 

## Future Improvements 
- Add authentication and authorization (JWT) 
- Switch to PostgreSQL for production 
- Add relationships between users and tasks with foreign key constraints 
- Implement more advanced query filtering and pagination 
- Add automated tests 

## Author 

Karel - Junior Python Developer 


