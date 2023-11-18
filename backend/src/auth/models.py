from sqlalchemy import (
    Integer,
    String,
)

from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


    task_owner = relationship("Branch", back_populates="owner")

    