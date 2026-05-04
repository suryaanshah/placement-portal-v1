from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/create-student")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.post("/create-employer")
def create_employer(employer: schemas.EmployerCreate, db: Session = Depends(get_db)):
    return crud.create_employer(db, employer)

@router.post("/add-skill")
def add_skill(skill: str, db: Session = Depends(get_db)):
    return crud.create_skill(db, skill)

@router.delete("/delete-skill/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    return crud.delete_skill(db, skill_id)

@router.delete("/delete-student/{student_roll_num}")
def delete_student(student_roll_num: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_roll_num)

@router.delete("/delete-employer/{employer_id}")
def delete_employer(employer_id: int, db: Session = Depends(get_db)):
    return crud.delete_employer(db, employer_id)
