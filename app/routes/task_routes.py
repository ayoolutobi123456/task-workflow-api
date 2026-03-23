from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        due_date=task.due_date,
        owner_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


def get_tasks(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
    return tasks


@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
        task_id: int,
        updated_task: TaskCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id

    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    task.priority = updated_task.priority
    task.due_date = updated_task.due_date

    db.commit()
    db.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}

# # @router.get("/tasks", response_model=list[TaskResponse])
# # def get_tasks(db: Session = Depends(get_db)):
# #     tasks = db.query(Task).all()
# #     return tasks
#
# @router.get("/tasks", response_model=list[TaskResponse])
# def get_tasks(
#         db: Session = Depends(get_db),
#         current_user: User = Depends(get_current_user)
# ):
#     tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
#     return tasks
#
#
# # @router.get("/tasks/{task_id}", response_model=TaskResponse)
# # def get_task(task_id: int, db: Session = Depends(get_db)):
# #     task = db.query(Task).filter(Task.id == task_id).first()
# #     return task
#
# @router.put("/tasks/{task_id}", response_model=TaskResponse)
# def update_task(task_id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#
#     task.title = updated_task.title
#     task.description = updated_task.description
#     task.status = updated_task.status
#
#     db.commit()
#     db.refresh(task)
#
#     return task
#
#
# @router.delete("/tasks/{task_id}")
# def delete_task(task_id: int, db: Session = Depends(get_db)):
#     task = db.query(Task).filter(Task.id == task_id).first()
#
#     db.delete(task)
#     db.commit()
#
#     return {"message": "Task deleted"}
