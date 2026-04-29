from sqlalchemy.orm import Session
from app.models.class_group import ClassGroup

def create_class_group(db: Session, cg):
    db_cg = ClassGroup(
        name=cg.name,
        classroom_id=cg.classroom_id
    )
    db.add(db_cg)
    db.commit()
    db.refresh(db_cg)
    return db_cg

def get_class_groups(db: Session):
    return db.query(ClassGroup).all()