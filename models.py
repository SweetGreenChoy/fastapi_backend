from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String, nullable=False, default="")
    description = Column(String, nullable=True, default="")
    ongoing = Column(Integer, nullable=False)
    winner = Column(Integer, ForeignKey("users.id"))


class Register(Base):
    __tablename__ = "registers"

    id = Column(Integer, ForeignKey("users.id", "tournaments.id"), primary_key=True)
    

class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    b_player = Column(Integer, ForeignKey("users.id"))
    w_player = Column(Integer, ForeignKey("users.id"))
    g_round = Column(Integer, nullable=False)
    winner = Column(Integer, ForeignKey("users.id"))
