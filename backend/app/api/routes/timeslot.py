from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.timeslot import TimeSlotCreate, TimeSlotOut
from app.services import timeslot_service
from app.models.timeslot import TimeSlot

router = APIRouter(prefix="/timeslots", tags=["TimeSlots"])

@router.post("/", response_model=TimeSlotOut)
def create_timeslot(timeslot: TimeSlotCreate, db: Session = Depends(get_db)):
    return timeslot_service.create_timeslot(db, timeslot)

@router.get("/", response_model=list[TimeSlotOut])
def get_timeslots(db: Session = Depends(get_db)):
    return timeslot_service.get_timeslots(db)


@router.put("/timeslots/fix-format")
def fix_hour_format(db: Session = Depends(get_db)):
    timeslots = db.query(TimeSlot).all()

    for ts in timeslots:
        if ts.hour and "." in ts.hour:
            ts.hour = ts.hour.replace(".", ":")

    db.commit()
    return {"message": "Hour format fixed"}