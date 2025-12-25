from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session  
from database import SessionLocal, engine 
import models, schemas 

app = FastAPI()

models.Base.metadata.create_all(bind = engine) # create tables if not exists 

def get_db():
    db = SessionLocal() # open session 
    try:
        yield db # session -> endpoint 
    finally: 
        db.close() # close session 

# create user 
@app.post("/users", response_model = schemas.UserPublic) 
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    db_user = models.User(name=user.name) 
    db.add(db_user) 
    db.commit()
    db.refresh(db_user) 
    return db_user

# get users
@app.get("/users", response_model = list[schemas.UserPublic]) 
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users 

# get user by id 
@app.get("/users/{user_id}", response_model = schemas.UserPublic)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first() 
    if not user: 
        raise HTTPException(status_code = 404, detail = "User not found!") 
    return user  

# update user 
@app.put("/users/{user_id}", response_model = schemas.UserPublic) 
def update_user(user_id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)): 
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found!") 
    user.name = updated_user.name 
    db.commit()
    db.refresh(user)
    return user 

# delete user 
@app.delete("/users/{user_id}", response_model = schemas.UserPublic) 
def delete_user(user_id: int, db: Session = Depends(get_db)): 
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found!")
    db.delete(user)
    db.commit()
    return user 

# create task 
@app.post("/tasks", response_model = schemas.TaskPublic) 
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        title = task.title,
        description = task.description,
        completed = False, 
        user_id = task.user_id 
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task 

# get tasks 
@app.get("/tasks", response_model = list[schemas.TaskPublic]) 
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks 

# get task by id 
@app.get("/tasks/{task_id}", response_model = schemas.TaskPublic)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404, detail = "Task not found!") 
    return task 

# update tasks 
@app.put("/tasks/{task_id}", response_model = schemas.TaskPublic) 
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task: 
        raise HTTPException(status_code = 404, detail = "Task not found!")
    task.title = updated_task.title 
    task.description = updated_task.description
    task.user_id = updated_task.user_id
    db.commit()
    db.refresh(task)
    return task 

@app.delete("/tasks/{task_id}", response_model = schemas.TaskPublic)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code = 404, detail = "Task not found!")
    db.delete(task)
    db.commit()
    return task 