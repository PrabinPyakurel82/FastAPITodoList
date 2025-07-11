# FastAPITodoList

## Project Overview
This is a backend API for a personal To-Do List application built using FastAPI. It allows users to register, log in, and manage their to-do items securely.

## Features

- User registration and login with JWT authentication
- Create, read, update, and delete to-do items
- Each user can only access their own to-dos
- PostgreSQL as the database with SQLAlchemy ORM
- Automatic timestamps for task creation and updates

## Setup Instructions

### Prerequisites

- Python 3.10+
- PostgreSQL installed and running

---

### 1. Clone the repository

```bash
git clone https://github.com/PrabinPyakurel82/FastAPITodoList.git
cd FastAPITodoList
```

### 2. Create and activate the virtual environment
```bash 
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file and add following
```bash
DATABASE_URL=postgresql://your_db_user:your_db_password@localhost/your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


### 5. Run the application
cd app
uvicorn main:app --reload


### 6. API Documentation

After starting the server, you can access the interactive API documentation at:

- `http://localhost:8000/docs` – Swagger UI (for testing endpoints)
- `http://localhost:8000/redoc` – ReDoc (for reference documentation)



## API Endpoints

### Authentication

#### Register new user

- **URL:** `/auth/register`
- **Method:** `POST`
- **Body:**
```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "yourpassword"
}
```

- **Response:**
```json
{
  "id": 1,
  "full_name": "John Doe",
  "email": "john@example.com"
}
```

#### Login

- **URL:** `/auth/login`
- **Method:** `POST`
- **Body:**
```json
{
  "username": "john@example.com",
  "password": "yourpassword"
}
  ```

- **Response:**
```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

### Todo operations

#### Get todos list
- **URL:** `/todos`
- **Method:** `GET`
- **Headers**
  Authorization: Bearer <access_token>

- **Response:**
```json
[
{
  "id": 1,
  "task": "Buy groceries",
  "completed": false,
  "created_at": "2025-07-11T12:00:00",
  "updated_at": "2025-07-11T12:00:00"
}
]
```

#### Create todo
- **URL:** `/todos`
- **Method:** `POST`
- **Headers**
  Authorization: Bearer <access_token>
- **Body:**
```json
{
    "task": "your-task-description"
}
  ```

- **Response:**
```json
[
{
  "id": 2,
  "task": "your-task-description",
  "completed": false,
  "created_at": "2025-07-11T12:05:00",
  "updated_at": "2025-07-11T12:05:00"
}
]
```

#### Update todo
- **URL:** `/todos/{todo_id}`
- **Method:** `PUT`
- **Headers**
  Authorization: Bearer <access_token>
- **Body:**
```json
{
  "task": "new-task-description",
  "completed": true
}
  ```

- **Response:**
```json
{
  "id": 2,
  "task": "new-task-description",
  "completed": true,
  "created_at": "2025-07-11T12:05:00",
  "updated_at": "2025-07-11T12:05:00"
}
```

#### Delete todo
- **URL:** `/todos/{todo_id}`
- **Method:** `DELETE`
- **Headers**
  Authorization: Bearer <access_token>

- **Response:**
Code: 204 No Content







