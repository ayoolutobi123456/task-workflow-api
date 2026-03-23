from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskCreate(BaseModel):
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    priority: TaskPriority
    due_date: datetime | None
    owner_id: int

    class Config:
        from_attributes = True
