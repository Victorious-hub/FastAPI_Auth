from sqlalchemy import (
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from database import Base


class Branch(Base):
    __tablename__ = "branch"

    id = Column(Integer, primary_key=True)
    branch_name = Column(String, nullable=False)
    description = Column(String,nullable=False)

    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("Users", back_populates="task_owner")

    # task = relationship("Task", back_populates="branch")

# class Task(Base):
#   __tablename__ = "task"
#
#    id = Column(Integer,primary_key=True)
#    title = Column(String, index=True)
#    description = Column(String, index=True)

#    owner_id = Column(Integer, ForeignKey("user.id"))
#    owner = relationship("Users", back_populates="task_owner")

#    branch_id = Column(Integer, ForeignKey("branch.id"))
#    branch = relationship("Branch", back_populates="task")

