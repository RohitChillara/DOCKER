from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum
from database import Base
import enum

class Status(enum.Enum):
    todo="todo"
    in_progress="in_progress"
    finished="finished"

class Task(Base):
    # todo: add create_constraint=True to enforce status values at the DB level
    # (currently only enforced in Python — fine while SQLAlchemy is the only writer)
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column(nullable=False,index=True)
    status:Mapped[Status]=mapped_column(SQLEnum(Status), default=Status.todo, nullable=False,index=True)