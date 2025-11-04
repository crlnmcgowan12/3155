# Assignment5/api/crud.py

from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Session

# runtime import only for models
import api.models as models

if TYPE_CHECKING:
    # only for type hints during static checking - won't be executed at runtime
    import api.schemas as schemas


# --- User CRUD Functions ---
def get_user(db: Session, user_id: int) -> models.User | None:
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: "schemas.UserCreate") -> models.User:
    db_user = models.User(name=user.name, age=user.age, gender=user.gender)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# --- Todo CRUD Functions ---
def get_todos(db: Session, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    return db.query(models.Todo).offset(skip).limit(limit).all()

def create_user_todo(db: Session, todo: "schemas.TodoCreate", user_id: int) -> models.Todo:
    # todo is a Pydantic model, so use model_dump() (v2) or .dict() for v1
    todo_data = todo.model_dump() if hasattr(todo, "model_dump") else todo.dict()
    db_todo = models.Todo(**todo_data)
    db_todo.user_id = user_id
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
