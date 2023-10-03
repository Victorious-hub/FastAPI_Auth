from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from starlette import status
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from database import get_db
from .models import Users
from .schemas import UserSchema
from fastapi import Depends, HTTPException

"""def hash_password(password: str) -> str:
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)

    # Return the hashed password as a string
    return hashed_password.decode("utf-8")"""

router = APIRouter(
    prefix='/user',
    tags=['user']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=None)
async def user_register(user: UserSchema, db: Session = Depends(get_db)):
    existing_email = db.query(Users).filter(Users.email == user.email).first()
    existing_user = db.query(Users).filter(Users.username == user.username).first()

    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists")
    elif existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this username already exists")

    create_user_model = Users(
        username=user.username,
        email=user.email,
        password=pwd_context.hash(user.password)
    )

    db.add(create_user_model)
    db.commit()


@router.get("/users", status_code=status.HTTP_200_OK, response_model=None)
async def user_register(db: Session = Depends(get_db)):
    get_users = db.query(Users).all()
    return get_users



