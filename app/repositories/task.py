from sqlalchemy.orm import Session
from app.db.models.task import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, title: str, description: str | None, owner_id: int):
        db_task = Task(title=title, description=description, owner_id=owner_id)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_all(self, owner_id: int | None = None):
        query = self.db.query(Task)
        if owner_id:
            query = query.filter(Task.owner_id == owner_id)
        return query.all()

    def get_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update(self, task_id: int, **kwargs):
        task = self.get_by_id(task_id)
        if task:
            for key, value in kwargs.items():
                if value is not None:
                    setattr(task, key, value)
            self.db.commit()
            self.db.refresh(task)
        return task

    def delete(self, task_id: int):
        task = self.get_by_id(task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
            return True
        return False