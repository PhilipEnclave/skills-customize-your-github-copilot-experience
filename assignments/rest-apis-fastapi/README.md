# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, applying core concepts like routing, request validation with Pydantic models, and CRUD operations to manage a collection of student records.

## 📝 Tasks

### 🛠️ Task 1: Set Up a FastAPI Application

#### Description
Create a basic FastAPI application with a root endpoint that returns a welcome message and a `/health` endpoint to confirm the server is running.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` application
- Define a `GET /` route that returns `{"message": "Welcome to the Student API"}`
- Define a `GET /health` route that returns `{"status": "ok"}`
- Be runnable with `uvicorn` on port 8000

### 🛠️ Task 2: Define a Student Model with Pydantic

#### Description
Define a `Student` data model using Pydantic's `BaseModel` to represent a student record, and create an in-memory list to store students.

#### Requirements
Completed program should:

- Define a `Student` model with fields: `id` (int), `name` (str), `grade` (int), and `email` (str)
- Validate that `grade` is between 1 and 12
- Initialize an in-memory list with at least two sample students

### 🛠️ Task 3: Implement CRUD Endpoints

#### Description
Add endpoints to create, read, update, and delete student records using the `Student` model and the in-memory list.

#### Requirements
Completed program should:

- `GET /students` — return all students
- `GET /students/{id}` — return a single student by ID, or return a 404 error if not found
- `POST /students` — accept a `Student` body and add it to the list
- `DELETE /students/{id}` — remove a student by ID, or return a 404 error if not found

Example response for `GET /students/1`:
```json
{"id": 1, "name": "Alice", "grade": 10, "email": "alice@school.edu"}
```

### 🛠️ Task 4: Add Query Parameter Filtering (Stretch Goal)

#### Description
Extend the `GET /students` endpoint to support optional filtering by grade level using a query parameter.

#### Requirements
Completed program should:

- Accept an optional `grade` query parameter on `GET /students`
- Return only students matching the specified grade when the parameter is provided
- Return all students when the parameter is omitted

Example: `GET /students?grade=10` returns only grade-10 students.
