from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.course import CourseCreate, CourseOut
from app.services import course_service

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return course_service.create_course(db, course)

@router.get("/", response_model=list[CourseOut])
def get_courses(db: Session = Depends(get_db)):
    return course_service.get_courses(db)