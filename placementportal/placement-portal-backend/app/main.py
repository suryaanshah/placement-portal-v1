from fastapi import FastAPI
from app.routes import admin_routes, student_routes, employer_routes
from app.database import engine, Base
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(admin_routes.router, prefix="/admin", tags=["admin"])
app.include_router(student_routes.router, prefix="/student", tags=["student"])
app.include_router(employer_routes.router, prefix="/employer", tags=["employer"])
