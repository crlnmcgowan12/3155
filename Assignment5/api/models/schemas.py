# In Assignment5/api/schemas.py

from pydantic import BaseModel
from typing import List, Optional

# --- User Schemas ---

class UserBase(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    # Define a relationship field for todos (if you have one)
    todos: List['Todo'] = []

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

# Update the forward reference for the User schema
User.model_rebuild()