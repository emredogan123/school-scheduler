from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str

from typing import Optional

from typing import List, Optional

class TeacherCreate(BaseModel):
    name: str
    available_slots: Optional[List[int]] = None

class TeacherOut(BaseModel):
    id: int
    name: str
    available_slots: Optional[List[int]] = None

    class Config:
        from_attributes = True  