from fastapi import APIRouter
from .schema import StudentCreateSchema, StudentUpdateSchema
from .storage import *

router = APIRouter()


@router.get("/")
async def root():
    return {"hello": "world"}

@router.post("/")
async def get_student(student_data: StudentCreateSchema, status_code=200):
    students_list.append(student_data)
    return student_data, status_code

@router.put("/{student_id}")
async def update_student(student: StudentUpdateSchema):
    return student

@router.get("/{student_id}")
async def get_data(student_id: int):
    return students_list[student_id]