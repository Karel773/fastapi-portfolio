from fastapi import FastAPI 
from database import Base, engine 
from routers import users, tasks 

# create tables if not exists 
Base.metadata.create_all(bind=engine) 

# FastAPI initialization 
app = FastAPI(
    title = "Task Manager API",
    description = "Simple backend API for managing users and their tasks",
    version = "1.0.0"
) 

# routers register 
app.include_router(users.router) 
app.include_router(tasks.router) 

# root endpoint 
@app.get("/", tags=["Root"]) 
def root():
    return {"message": "API works, check /docs"} 