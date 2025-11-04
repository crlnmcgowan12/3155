# In Assignment5/api/crud.py

from sqlalchemy.orm import Session
from typing import List

# Change to the correct, simple relative imports for modules in the same directory:
from . import models
from . import schemas


def get_user(db: Session, user_id: int):
    """Retrieves a single user by ID."""
    # Note: Added the import of models.User explicitly
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Retrieves a list of all users."""
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    """Creates a new user record in the database."""
    db_user = models.User(name=user.name, age=user.age, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Todo CRUD Functions ---

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    """Retrieves a list of all todo items."""
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_user_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    """Creates a new todo item associated with a specific user."""
    # Use model_dump() for Pydantic v2 or newer
    db_todo = models.Todo(**todo.model_dump()) 
    db_todo.user_id = user_id 
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo