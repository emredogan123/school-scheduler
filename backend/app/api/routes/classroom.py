from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.classroom import ClassroomCreate, ClassroomOut
from app.services import classroom_service

router = APIRouter(prefix="/classrooms", tags=["Classrooms"])

@router.post("/", response_model=ClassroomOut)
def create_classroom(classroom: ClassroomCreate, db: Session = Depends(get_db)):
    return classroom_service.create_classroom(db, classroom)

@router.get("/", response_model=list[ClassroomOut])
def get_classrooms(db: Session = Depends(get_db)):
    return classroom_service.get_classrooms(db)