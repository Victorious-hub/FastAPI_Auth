from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from starlette import status
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from database import get_db
from .models import *
from .schemas import *
from datetime import timedelta,datetime
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from pydantic import BaseModel

SECRET_KEY = '38759723759aqryq9yrqrhq09rq0wrq082104y120384'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')


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
dp_dependency = Annotated[Session, Depends(get_db)]

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

@router.post("/title", status_code=status.HTTP_201_CREATED, response_model=None)
async def user_register(user: TitleSchema, db: Session = Depends(get_db)):
   
    create_user_model = Title(
        title = user.title
    )

    db.add(create_user_model)
    db.commit()

def authenticate_user(username: str, password:str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password,user.password):
        return False
    return user


def create_access_token(username: str, user_id: int, expires_delta: timedelta):
    encode = {'sub':username, 'id':user_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)


@router.post('/token',response_model=None)
async def login_user(form_data: Annotated[OAuth2PasswordRequestForm,Depends()],
                     db:dp_dependency):

    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate')
    token = create_access_token(user.username,user.id,timedelta(minutes=20))
    return {'access_token':token,'token_type':'bearer'}