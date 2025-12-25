from sqlalchemy import Column, Integer, String, Boolean 
from database import Base # import base from database.py 

# create a users table
class User(Base): 
    __tablename__ = "users" 
    __table_args__ = {'extend_existing': True} 

    id = Column(Integer, primary_key = True, index = True) 
    name = Column(String, nullable = False) 
    is_active = Column(Boolean, default = True) 

# create a tasks table 
class Task(Base):
    __tablename__ = "tasks" 

    id = Column(Integer, primary_key = True, index = True) 
    title = Column(String, nullable = False) 
    description = Column(String, nullable = False) 
    completed = Column(Boolean, default = False) 
    user_id = Column(Integer, nullable = False) 