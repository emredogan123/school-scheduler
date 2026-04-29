from app.models.schedule import Schedule
from app.models.course import Course
from app.models.timeslot import TimeSlot
from app.models.teacher import Teacher
import random


def is_teacher_available(teacher, slot_id):
    if not teacher.available_slots:
        return False

    return slot_id in teacher.available_slots


def generate_schedule(db):

    # temizle
    db.query(Schedule).delete()
    db.commit()

    
    courses = db.query(Course).all()
    timeslots = db.query(TimeSlot).all()

    random.shuffle(courses)
    random.shuffle(timeslots)
    # 📊 usage tracking
    teacher_usage = {}   # (teacher_id, slot_id)
    class_usage = {}     # (class_id, slot_id)

    result = []
    conflicts = []

    def course_difficulty(course):
        teacher = course.teacher
        if not teacher or not teacher.available_slots:
            return 999
        return len(teacher.available_slots)

    courses.sort(key=course_difficulty)

    def backtrack(course_index):

        if course_index == len(courses):
            return True

        course = courses[course_index]
        teacher = course.teacher
        class_group = course.class_group

        assigned = 0

        for slot in timeslots:

            if assigned >= course.weekly_hours:
                break

            # ❌ teacher uygun değil
            if not is_teacher_available(teacher, slot.id):
                continue

            # ❌ teacher çakışma
            if (teacher.id, slot.id) in teacher_usage:
                continue

            # ❌ class çakışma
            if (class_group.id, slot.id) in class_usage:
                continue

            # ✅ assign
            schedule = Schedule(
                course_id=course.id,
                teacher_id=teacher.id,
                timeslot_id=slot.id
            )

            db.add(schedule)

            teacher_usage[(teacher.id, slot.id)] = True
            class_usage[(class_group.id, slot.id)] = True

            result.append(schedule)

            assigned += 1

        # ❌ eksik kaldıysa → fail
        if assigned < course.weekly_hours:
            conflicts.append({
                "course": course.name,
                "assigned": assigned,
                "required": course.weekly_hours
            })
            return False

        return backtrack(course_index + 1)

    backtrack(0)

    db.commit()

    return {
        "status": "done",
        "conflicts": conflicts
    }