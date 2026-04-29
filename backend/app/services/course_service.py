from sqlalchemy.orm import Session
from app.models.course import Course

def create_course(db: Session, course):
    db_course = Course(
        name=course.name,
        teacher_id=course.teacher_id,
        class_id=course.class_id,
        weekly_hours=course.weekly_hours
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses(db: Session):
    return db.query(Course).all()