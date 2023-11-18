from typing import Union, List, Optional
from pydantic import BaseModel, EmailStr

class BranchSchema(BaseModel):
    branch_name: str
    description: str
    owner_id: int