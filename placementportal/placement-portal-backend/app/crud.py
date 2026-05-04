from sqlalchemy.orm import Session
from app import models, schemas
from app.models import Skill, Student, Internship, Project

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(email=student.email, hashed_password=student.password)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_employer(db: Session, employer: schemas.EmployerCreate):
    db_employer = models.User(email=employer.email, hashed_password=employer.password, user_type='employer')
    db.add(db_employer)
    db.commit()
    db.refresh(db_employer)
    return db_employer

def create_skill(db: Session, skill: str):
    db_skill = models.Skill(name=skill)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def delete_skill(db: Session, skill_id: int):
    db_skill = db.query(Skill).filter(Skill.id == skill_id).first()
    db.delete(db_skill)
    db.commit()
    return db_skill

def add_skill_to_student(db: Session, student_roll_num: int, skill_id: int):
    student_skill = models.StudentSkills(student_roll_num=student_roll_num, skill_id=skill_id)
    db.add(student_skill)
    db.commit()
    db.refresh(student_skill)
    return student_skill

def remove_skill_from_student(db: Session, student_roll_num: int, skill_id: int):
    student_skill = db.query(models.StudentSkills).filter(models.StudentSkills.student_roll_num == student_roll_num, models.StudentSkills.skill_id == skill_id).first()
    db.delete(student_skill)
    db.commit()
    return student_skill

def create_internship(db: Session, internship: schemas.InternshipCreate, student_roll_num: int):
    db_internship = models.Internship(**internship.dict(), student_id=student_roll_num)
    db.add(db_internship)
    db.commit()
    db.refresh(db_internship)
    return db_internship

def delete_internship(db: Session, internship_id: int):
    db_internship = db.query(Internship).filter(Internship.id == internship_id).first()
    db.delete(db_internship)
    db.commit()
    return db_internship

def update_internship(db: Session, internship_id: int, internship: schemas.InternshipCreate):
    db_internship = db.query(Internship).filter(Internship.id == internship_id).first()
    for key, value in internship.dict().items():
        setattr(db_internship, key, value)
    db.commit()
    db.refresh(db_internship)
    return db_internship

def create_project(db: Session, project: schemas.ProjectCreate, student_roll_num: int):
    db_project = models.Project(**project.dict(), student_id=student_roll_num)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id: int):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    db.delete(db_project)
    db.commit()
    return db_project

def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    for key, value in project.dict().items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_student(db: Session, student_roll_num: int):
    db_student = db.query(Student).filter(Student.roll_num == student_roll_num).first()
    db.delete(db_student)
    db.commit()
    return db_student

def delete_employer(db: Session, employer_id: int):
    db_employer = db.query(models.User).filter(models.User.id == employer_id, models.User.user_type == "employer").first()
    db.delete(db_employer)
    db.commit()
    return db_employer
