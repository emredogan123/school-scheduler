from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class ClassGroup(Base):
    __tablename__ = "class_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    classroom_id = Column(Integer, ForeignKey("classrooms.id"))

    classroom = relationship("Classroom")