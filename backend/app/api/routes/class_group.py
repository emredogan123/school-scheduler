from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.class_group import ClassGroupCreate, ClassGroupOut
from app.services import class_group_service

router = APIRouter(prefix="/class-groups", tags=["ClassGroups"])

@router.post("/", response_model=ClassGroupOut)
def create_class_group(cg: ClassGroupCreate, db: Session = Depends(get_db)):
    return class_group_service.create_class_group(db, cg)

@router.get("/", response_model=list[ClassGroupOut])
def get_class_groups(db: Session = Depends(get_db)):
    return class_group_service.get_class_groups(db)