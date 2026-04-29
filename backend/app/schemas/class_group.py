from pydantic import BaseModel

class ClassGroupCreate(BaseModel):
    name: str
    classroom_id: int

class ClassGroupOut(BaseModel):
    id: int
    name: str
    classroom_id: int

    class Config:
        from_attributes = True