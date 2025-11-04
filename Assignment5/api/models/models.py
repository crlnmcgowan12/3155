# Assignment5/api/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base  # assuming database.py defines Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    day = Column(Integer, nullable=True)
    month = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # note: match "users" not "user"

    owner = relationship("User", back_populates="todos")
