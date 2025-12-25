from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
# database connection and create a file 
engine = create_engine("sqlite:///test.db", echo=True) 
# ORM model declaration 
Base = declarative_base() 
# Session maker 
SessionLocal = sessionmaker(bind = engine, autocommit = False, autoflush = False) 