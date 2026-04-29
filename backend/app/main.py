from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes.teacher import router as teacher_router
from app.api.routes.classroom import router as classroom_router
from app.api.routes.course import router as course_router
from app.api.routes.timeslot import router as timeslot_router

from app.api.routes.schedule import router as schedule_router

from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import class_group

from app.models import teacher, classroom, course, timeslot, schedule  # noqa

app = FastAPI()


app.include_router(teacher_router)
app.include_router(classroom_router)
app.include_router(course_router)
app.include_router(timeslot_router)

app.include_router(schedule_router)

app.include_router(class_group.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://school-scheduler-lac.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Scheduler API is running"}

