<<<<<<< HEAD
﻿from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        title = value.strip()
        if len(title) < 3:
            raise ValueError("Task title must contain at least 3 characters")
        return title

=======
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"

class TaskCreate(TaskBase):
    pass
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

<<<<<<< HEAD
    @field_validator("status")
    @classmethod
    def validate_status(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        allowed = {"new", "in_progress", "done"}
        if value not in allowed:
            raise ValueError(f"Status must be one of: {allowed}")
        return value


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
=======
class TaskOut(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
