from pydantic import BaseModel

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    first_name: str or None
    last_name: str or None