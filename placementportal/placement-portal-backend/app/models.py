from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Table

# Association Table for many-to-many relationship between students and skills
student_skills = Table(
    'student_skills',
    Base.metadata,
    Column('student_roll_num', Integer, ForeignKey('students.roll_num'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    roll_num = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    skills = relationship("Skill", secondary=student_skills, back_populates="students")
    internships = relationship("Internship", back_populates="student")
    projects = relationship("Project", back_populates="student")

class Skill(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    students = relationship("Student", secondary=student_skills, back_populates="skills")

class Internship(Base):
    __tablename__ = 'internships'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    start_date = Column(String)
    end_date = Column(String)
    place = Column(String)
    professor_name = Column(String)
    description = Column(String)
    student_roll_num = Column(Integer, ForeignKey('students.roll_num'))

    student = relationship("Student", back_populates="internships")

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    start_date = Column(String)
    end_date = Column(String)
    place = Column(String)
    description = Column(String)
    student_roll_num = Column(Integer, ForeignKey('students.roll_num'))

    student = relationship("Student", back_populates="projects")
