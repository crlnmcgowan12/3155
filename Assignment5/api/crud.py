# In Assignment5/api/crud.py

from sqlalchemy.orm import Session
from . import models, schemas # Imports models.py and schemas.py from the current package
from typing import List

# --- User CRUD Functions ---

def get_user(db: Session, user_id: int) -> models.User | None:
    """Retrieves a single user by ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    """Retrieves a list of all users."""
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """Creates a new user record in the database."""
    # Note: If your models.py uses an auto-incrementing ID, you don't pass the ID here
    db_user = models.User(name=user.name, age=user.age, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# --- Todo CRUD Functions ---

def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    """Retrieves a list of all todo items."""
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_user_todo(db: Session, todo: schemas.TodoCreate, user_id: int) -> models.Todo:
    """Creates a new todo item associated with a specific user."""
    # Unpack the data from the Pydantic schema
    db_todo = models.Todo(**todo.model_dump()) 
    db_todo.user_id = user_id # Manually set the foreign key
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo