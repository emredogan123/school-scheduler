from sqlalchemy.orm import Session
from app.models.classroom import Classroom
from app.schemas.classroom import ClassroomCreate

def create_classroom(db: Session, classroom: ClassroomCreate):
    db_classroom = Classroom(name=classroom.name)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def get_classrooms(db: Session):
    return db.query(Classroom).all()