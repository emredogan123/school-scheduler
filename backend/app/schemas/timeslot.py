from pydantic import BaseModel

class TimeSlotBase(BaseModel):
    day: str
    hour: str

class TimeSlotCreate(TimeSlotBase):
    pass

class TimeSlotOut(TimeSlotBase):
    id: int

    class Config:
        from_attributes = True