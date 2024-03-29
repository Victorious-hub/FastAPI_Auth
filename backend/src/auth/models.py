from sqlalchemy import (
    Integer,
    String,
)

from sqlalchemy.sql.schema import Column

from database import Base


class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    