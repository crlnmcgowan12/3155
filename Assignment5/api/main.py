# Assignment5/api/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import api.crud as crud
import api.models as models
import api.schemas as schemas
from .database import SessionLocal, engine

# create tables (safe no-op if they already exist)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- User Endpoints ---
@app.post("/users/", response_model=schemas.User)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


# --- Todo Endpoints ---
@app.post("/users/{user_id}/todos/", response_model=schemas.Todo)
def create_todo_for_user(user_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_user_todo(db=db, todo=todo, user_id=user_id)

@app.get("/todos/", response_model=List[schemas.Todo])
def read_todos_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos
