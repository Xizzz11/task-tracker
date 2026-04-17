<<<<<<< HEAD
﻿from fastapi import FastAPI

from app1.api.routers import admin, auth, tasks
from app1.core.database import Base, engine

# app = FastAPI(title="Task API")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.on_event("startup")
def on_startup() -> None:
    import app1.models.task  # noqa: F401
    import app1.models.user  # noqa: F401

    Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(admin.router)
=======
from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth, tasks, admin

app = FastAPI(
    title="Task Tracker API",
    description="Практическая работа: монолит → чистая архитектура",
    version="1.0.0"
)

# Подключаем роутеры
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
async def root():
    return {"message": "Task Tracker API is running. Go to /docs"}
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
