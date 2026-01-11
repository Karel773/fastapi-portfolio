from pydantic import BaseModel, Field
from typing import Optional  

# create a user and task schemas 

class UserCreate(BaseModel): 
    name: str = Field(..., min_length= 2, max_length = 50, description = "Username must be 2-50 characters long") 
    password: str = Field(..., min_length = 6, max_length = 72) 

class UserPublic(BaseModel):
    id: int 
    name: str 
    is_active: bool 

    class Config:
        from_attributes = True 

class TaskCreate(BaseModel):
    title: str = Field(..., min_length = 1, max_length = 100) 
    description: Optional[str] = Field(default = None, max_length = 300) 
    user_id: int = Field(..., gt = 0)

class TaskPublic(BaseModel):
    id: int 
    title: str 
    description: Optional[str]
    completed: bool 
    user_id: int 

    class Config:
        from_attributes = True 

class Token(BaseModel):
    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    user_id: Optional[int] = None