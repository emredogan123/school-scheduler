from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    teacher_id: int
    class_id: int
    weekly_hours: int

class CourseOut(BaseModel):
    id: int
    name: str
    teacher_id: int
    class_id: int
    weekly_hours: int

    class Config:
        from_attributes = True