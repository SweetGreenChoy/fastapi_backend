from uuid import UUID
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base

""" 
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

"""

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(UUID, nullable=False)
    name = Column(String, nullable=False)
    points = Column(Integer, nullable=False, default=1000000)
    rp = Column(Integer, nullable=False)


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, default="")
    description = Column(String, nullable=True, default="")
    created = Column(datetime.timestamp, nullable=True,)
    ongoing = Column(Integer, nullable=False)
    winner = Column(Integer, ForeignKey("players.id"))


class Register(Base):
    __tablename__ = "registers"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.key"))
    tournament_id = Column(Integer, ForeignKey("tournaments.id"), index=True)
    

class Battle(Base):
    __tablename__ = "battles"

    id = Column(Integer, primary_key=True, index=True)
    b_player = Column(Integer, ForeignKey("players.id"))
    w_player = Column(Integer, ForeignKey("players.id"))
    g_round = Column(Integer, nullable=False)
    winner = Column(Integer, ForeignKey("players.id"))