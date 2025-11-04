# Assignment5/api/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(255), nullable=True)

    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    day = Column(Integer, nullable=True)
    month = Column(String(255), nullable=True)
    year = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="todos")
