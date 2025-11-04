# Assignment5/api/schemas.py

from pydantic import BaseModel
from typing import Optional

# --- User Schemas ---
class UserBase(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# --- Todo Schemas ---
class TodoBase(BaseModel):
    title: str
    day: Optional[int] = None
    month: Optional[str] = None
    year: Optional[int] = None
    user_id: int

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int

    class Config:
        from_attributes = True
