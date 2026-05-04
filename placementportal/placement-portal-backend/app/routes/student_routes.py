from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/add-skill/{student_roll_num}")
def add_skill(student_roll_num: int, skill_id: int, db: Session = Depends(get_db)):
    return crud.add_skill_to_student(db, student_roll_num, skill_id)

@router.delete("/delete-skill/{student_roll_num}")
def remove_skill(student_roll_num: int, skill_id: int, db: Session = Depends(get_db)):
    return crud.remove_skill_from_student(db, student_roll_num, skill_id)

@router.post("/add-internship")
def add_internship(internship: schemas.InternshipCreate, student_roll_num: int, db: Session = Depends(get_db)):
    return crud.create_internship(db, internship, student_roll_num)

@router.delete("/delete-internship/{internship_id}")
def delete_internship(internship_id: int, db: Session = Depends(get_db)):
    return crud.delete_internship(db, internship_id)

@router.put("/update-internship/{internship_id}")
def update_internship(internship_id: int, internship: schemas.InternshipCreate, db: Session = Depends(get_db)):
    return crud.update_internship(db, internship_id, internship)

@router.post("/add-project")
def add_project(project: schemas.ProjectCreate, student_roll_num: int, db: Session = Depends(get_db)):
    return crud.create_project(db, project, student_roll_num)

@router.delete("/delete-project/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return crud.delete_project(db, project_id)

@router.put("/update-project/{project_id}")
def update_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.update_project(db, project_id, project)
