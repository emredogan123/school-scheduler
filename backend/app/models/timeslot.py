from sqlalchemy import Column, Integer, String
from app.db.database import Base

class TimeSlot(Base):
    __tablename__ = "timeslots"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(String)
    hour = Column(String)