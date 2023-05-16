from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

@app.get("/")
async def root():
    return {"hello": ""}

@app.post("/students")
async def get_student(student_data: StudentCreateSchema, status_code=200):
    return student_data, status_code