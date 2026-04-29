from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.timeslot import TimeSlotCreate, TimeSlotOut
from app.services import timeslot_service

router = APIRouter(prefix="/timeslots", tags=["TimeSlots"])

@router.post("/", response_model=TimeSlotOut)
def create_timeslot(timeslot: TimeSlotCreate, db: Session = Depends(get_db)):
    return timeslot_service.create_timeslot(db, timeslot)

@router.get("/", response_model=list[TimeSlotOut])
def get_timeslots(db: Session = Depends(get_db)):
    return timeslot_service.get_timeslots(db)