from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session
from starlette import status
from fastapi import Depends, HTTPException
from database import get_db
from .models import *
from .schemas import *
from src.auth.models import Users
from src.auth.router import get_current_user
from src.auth.schemas import UserSchema
from .schemas import BranchSchema

router = APIRouter(
    prefix = '/api/tasks',
    tags=['tasks']
)

@router.post('/create_branch',status_code=status.HTTP_200_OK, response_model=None)
def create_branch(branch: BranchSchema, db: Session = Depends(get_db),current_user: Users = Depends(get_current_user)):
    current_user = UserSchema(
        id = current_user.id,
        username=current_user.username,
        email=current_user.email,
        password = current_user.password
    )
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    create_user_branch = BranchSchema(
        branch_name=branch.branch_name,
        description=branch.description,
        owner_id=current_user.id  # Set the owner_id to the ID of the current authenticated user
    )

    db_branch = Branch(**create_user_branch.dict())  # Assuming you have a Branch model

    db.add(db_branch)
    db.commit()

    
@router.get('/branches',status_code=status.HTTP_200_OK, response_model=None)
async def create_branch(db: Session = Depends(get_db),current_user: Users = Depends(get_current_user)):
    current_user = UserSchema(
        id = current_user.id,
        username=current_user.username,
        email=current_user.email,
        password = current_user.password
    )
    if not current_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")

    get_branches = db.query(Branch).all()
    return get_branches
    
    