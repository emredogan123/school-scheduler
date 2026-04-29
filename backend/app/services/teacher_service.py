from sqlalchemy.orm import Session
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate

def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(
    name=teacher.name,
    available_slots=teacher.available_slots)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teachers(db: Session):
    return db.query(Teacher).all()