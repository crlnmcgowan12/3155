# In Assignment5/api/schemas.py

from pydantic import BaseModel
from typing import Optional, List # Combined List and Optional import

# --- User Schemas ---

class UserBase(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    # Removed the 'todos: List['Todo']' line to prevent circular dependency
    
    # CRITICAL: Tells Pydantic to read data from SQLAlchemy model (ORM)
    class Config:
        from_attributes = True


# --- Todo Schemas ---

class TodoBase(BaseModel):
    title: str
    day: Optional[int] = None
    month: Optional[str] = None
    year: Optional[int] = None
    user_id: int  # The foreign key

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    
    # CRITICAL: Tells Pydantic to read data from SQLAlchemy model (ORM)
    class Config:
        from_attributes = True

# Removed the User.model_rebuild() call