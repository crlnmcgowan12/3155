# In Assignment5/api/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

# --- User CRUD (Read function) ---
def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    # This reads the user data you inserted earlier
    return db.query(models.User).offset(skip).limit(limit).all()

# --- Todo CRUD (Read function) ---
def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    # This reads the todo data you inserted earlier
    return db.query(models.Todo).offset(skip).limit(limit).all()

# You can add the rest of your CRUD logic (create/update/delete) later, 
# but these two functions fix the import error and allow you to test your GET endpoints.