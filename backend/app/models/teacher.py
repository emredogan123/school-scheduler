from sqlalchemy import Column, Integer, String, JSON
from app.db.database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    available_slots = Column(JSON)   