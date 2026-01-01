from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
import models 
import schemas 

router = APIRouter(
    prefix = "/users",
    tags  = ["Users"] 
)

# session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create user
@router.post("/", response_model=schemas.UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# read all users
@router.get("/", response_model=list[schemas.UserPublic])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# read user by id
@router.get("/{user_id}", response_model=schemas.UserPublic)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

# update user
@router.put("/{user_id}", response_model=schemas.UserPublic)
def update_user(user_id: int, updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    user.name = updated_user.name
    db.commit()
    db.refresh(user)
    return user

# delete user
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    db.delete(user)
    db.commit()