from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

# TODO: Instantiate the FastAPI app
app = FastAPI()

# TODO: Define a Student model using Pydantic BaseModel
# Fields: id (int), name (str), grade (int, between 1-12), email (str)
class Student(BaseModel):
    id: int
    name: str
    grade: int = Field(..., ge=1, le=12)
    email: str

# TODO: Create an in-memory list with at least two sample students
students = []

# TODO: Task 1 — Add a GET / route that returns a welcome message
@app.get("/")
def root():
    pass

# TODO: Task 1 — Add a GET /health route that returns {"status": "ok"}
@app.get("/health")
def health():
    pass

# TODO: Task 3 — GET /students — return all students
# (Stretch: accept an optional `grade` query parameter to filter results)
@app.get("/students")
def get_students(grade: Optional[int] = None):
    pass

# TODO: Task 3 — GET /students/{id} — return a student by ID or raise 404
@app.get("/students/{student_id}")
def get_student(student_id: int):
    pass

# TODO: Task 3 — POST /students — add a new student from the request body
@app.post("/students")
def create_student(student: Student):
    pass

# TODO: Task 3 — DELETE /students/{id} — remove a student by ID or raise 404
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
