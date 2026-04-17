from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.services.task_service import TaskService
from app.core.security import get_current_user


router = APIRouter()

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return TaskService(db).create_task(task.title, task.description, current_user.id)

@router.get("/", response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return TaskService(db).get_tasks(current_user.id)

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return TaskService(db).get_task(task_id)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return TaskService(db).update_task(task_id, **task.model_dump(exclude_unset=True))

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return TaskService(db).delete_task(task_id)