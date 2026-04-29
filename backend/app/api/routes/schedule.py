from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.scheduler.scheduler import generate_schedule

from app.models.schedule import Schedule
from app.models.course import Course
from app.models.timeslot import TimeSlot
from app.models.class_group import ClassGroup
from app.models.teacher import Teacher

router = APIRouter(prefix="/schedule", tags=["Schedule"])

@router.post("/generate")
def generate(db: Session = Depends(get_db)):
    result = generate_schedule(db)
    return result
@router.get("/")
def get_schedule(db: Session = Depends(get_db)):
    schedules = db.query(Schedule).all()

    result = []

    for s in schedules:
        if not (s.course and s.timeslot):
            continue

        result.append({
            "course": s.course.name,
            "teacher": s.course.teacher.name,
            "class": s.course.class_group.name,
            "classroom": s.course.class_group.classroom.name,
            "day": s.timeslot.day,
            "hour": s.timeslot.hour
        })

    return result

@router.get("/grid")
def get_schedule_grid(db: Session = Depends(get_db)):

    schedules = db.query(Schedule).all()
    timeslots = db.query(TimeSlot).all()
    classes = db.query(ClassGroup).all()

    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    days = sorted(
        list(set(ts.day for ts in timeslots)),
        key=lambda d: day_order.index(d) if d in day_order else 999
    )

    hours = sorted(
        list(set(ts.hour for ts in timeslots)),
        key=lambda h: int(h.split(":")[0])
    )

    class_names = [c.name for c in classes]

    # GRID
    grid = {
        class_name: {
            hour: {day: None for day in days}
            for hour in hours
        }
        for class_name in class_names
    }

    # Fill grid
    for s in schedules:

        if not (s.course and s.timeslot):
            continue

        class_name = s.course.class_group.name

        grid[class_name][s.timeslot.hour][s.timeslot.day] = {
            "course": s.course.name,
            "teacher": s.course.teacher.name,
            "classroom": s.course.class_group.classroom.name
        }

    return {
        "classes": class_names,
        "days": days,
        "hours": hours,
        "grid": grid
    }