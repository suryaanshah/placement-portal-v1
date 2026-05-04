from pydantic import BaseModel

class Login(BaseModel):
    email: str
    password: str

class StudentCreate(BaseModel):
    email: str
    password: str

class EmployerCreate(BaseModel):
    email: str
    password: str

class InternshipCreate(BaseModel):
    title: str
    start_date: str
    end_date: str
    place: str
    professor_name: str
    description: str

class ProjectCreate(BaseModel):
    title: str
    start_date: str
    end_date: str
    place: str
    description: str
