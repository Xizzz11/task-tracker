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