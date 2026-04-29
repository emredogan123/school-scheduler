from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.teacher import TeacherCreate, TeacherOut
from app.services import teacher_service

router = APIRouter(prefix="/teachers", tags=["Teachers"])

@router.post("/", response_model=TeacherOut)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return teacher_service.create_teacher(db, teacher)

@router.get("/", response_model=list[TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    return teacher_service.get_teachers(db)