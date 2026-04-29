from sqlalchemy.orm import Session
from app.models.timeslot import TimeSlot
from app.schemas.timeslot import TimeSlotCreate

def create_timeslot(db: Session, timeslot: TimeSlotCreate):
    db_timeslot = TimeSlot(day=timeslot.day, hour=timeslot.hour)
    db.add(db_timeslot)
    db.commit()
    db.refresh(db_timeslot)
    return db_timeslot

def get_timeslots(db: Session):
    return db.query(TimeSlot).all()