from sqlalchemy.orm import Session
from app.repositories.task import TaskRepository

class TaskService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = TaskRepository(db)

    def create_task(self, title: str, description: str | None, owner_id: int):
        return self.repo.create(title, description, owner_id)

    def get_tasks(self, owner_id: int | None = None):
        return self.repo.get_all(owner_id)

    def get_task(self, task_id: int):
        task = self.repo.get_by_id(task_id)
        if not task:
            raise Exception("Task not found")
        return task

    def update_task(self, task_id: int, **kwargs):
        task = self.repo.update(task_id, **kwargs)
        if not task:
            raise Exception("Task not found")
        return task

    def delete_task(self, task_id: int):
        if not self.repo.delete(task_id):
            raise Exception("Task not found")
        return {"detail": "Task deleted"}