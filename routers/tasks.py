from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session 
from database import SessionLocal 
import models
import schemas 
from security import get_current_user

router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"]
)

# session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create task
@router.post("/", response_model=schemas.TaskPublic, status_code = status.HTTP_201_CREATED) 
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: schemas.UserPublic = Depends(get_current_user)): 
    db_task = models.Task(
        title=task.title,
        description=task.description,
        completed=False,
        user_id=current_user.id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# read all tasks
@router.get("/", response_model=list[schemas.TaskPublic])
def get_tasks(db: Session = Depends(get_db), current_user: schemas.UserPublic = Depends(get_current_user)): 
    tasks = db.query(models.Task).filter(models.Task.user_id == current_user.id).all()
    return tasks 

# read task by id
@router.get("/{task_id}", response_model=schemas.TaskPublic)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# update task
@router.put("/{task_id}", response_model=schemas.TaskPublic)
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: schemas.UserPublic = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found") 
    if task.user_id != current_user.id: 
        raise HTTPException(status_code=403, detail="Not authorized to update this task!") 
    task.title = updated_task.title
    task.description = updated_task.description
    task.user_id = updated_task.user_id
    db.commit()
    db.refresh(task)
    return task

# delete task
@router.delete("/{task_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: schemas.UserPublic = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if  task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this task!")
    db.delete(task)
    db.commit()
