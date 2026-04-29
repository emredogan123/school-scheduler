from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)

    course_id = Column(Integer, ForeignKey("courses.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    class_id = Column(Integer, ForeignKey("class_groups.id"))
    timeslot_id = Column(Integer, ForeignKey("timeslots.id"))

    course = relationship("Course")
    teacher = relationship("Teacher")
    class_group = relationship("ClassGroup")
    timeslot = relationship("TimeSlot")