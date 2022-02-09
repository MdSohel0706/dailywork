from sqlalchemy import Boolean, Column, Integer, String
from xmlrpc.client import Boolean
from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy
from typing import List, Optional
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#----------------------------------------------------
SQLALCHEMY_DATABASE_URL = "mysql://sohel:tiger@localhost/fastapitodo"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind = engine)
#----------------------------------------------------
app = FastAPI()

#----------------------------------------------------

class Item(BaseModel):
    __tablename__ = "tododata"
    id = Column(Integer, primary_key = True, index = True)
    task = Column(String, unique = True)
    description = Column(String)
    finished = Column(Boolean)
#----------------------------------------------------
#creating pydantic models

class ItemBase(BaseModel):
    task : str
    decription : Optional[str] = None 
    finished : bool

#----------------------------------------------------
def get_db():
    db = None 
    try : 
        db = SessionLocal()
        yield db
    finally:
        db.close()
#----------------------------------------------------


@app.post("/items")
def create_item(item: Item):
    return "Item Created"

@app.get("/items/{item_id}")
def read_item(item_id: str):
    return "Item Retrieved"

@app.get("/all_items")
def get_all_items():
    return "All items retrieved"

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8000)
