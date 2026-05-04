from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import get_db

router = APIRouter()

@router.post("/login")
async def employer_login(credentials: schemas.Login, db: Session = Depends(get_db)):
    return crud.employer_login(db=db, credentials=credentials)
