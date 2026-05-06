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

    # 🔥 eski schedule'ı temizle (en önemli fix)
    db.query(Schedule).delete()
    db.commit()

    result = generate_schedule(db)
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

    # GRID oluştur
    grid = {
        class_name: {
            hour: {day: None for day in days}
            for hour in hours
        }
        for class_name in class_names
    }

    # 🔥 SAFE FILL (CRASH ENGELLEYEN KISIM)
    for s in schedules:

        if not (s.course and s.timeslot):
            continue

        if not (s.course.class_group and s.course.teacher):
            continue

        class_name = s.course.class_group.name
        hour = s.timeslot.hour
        day = s.timeslot.day

        # 🔥 KEY CHECK (EN KRİTİK)
        if (
            class_name not in grid
            or hour not in grid[class_name]
            or day not in grid[class_name][hour]
        ):
            continue

        grid[class_name][hour][day] = {
            "course": s.course.name,
            "teacher": s.course.teacher.name,
            "classroom": (
                s.course.class_group.classroom.name
                if s.course.class_group.classroom else None
            )
        }

    return {
        "classes": class_names,
        "days": days,
        "hours": hours,
        "grid": grid
    }