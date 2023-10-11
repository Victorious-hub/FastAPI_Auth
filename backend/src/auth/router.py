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
from jose import JWTError, jwt
from pydantic import BaseModel

SECRET_KEY = '38759723759aqryq9yrqrhq09rq0wrq082104y120384'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/token')

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

def get_password(password,hashed_password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)
    def verify(hashed_password,plain_password):
        return pwd_context.verify(plain_password,hashed_password)

@router.post('/token',tags=['authentication'],status_code=status.HTTP_202_ACCEPTED,response_model = Token)
def login(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    print(request.username)
    user=db.query(Users).filter(Users.username ==request.username).first()
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,\
                            detail=f"Invalid Credential-User")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,\
                            detail=f"Invalid Credential-Pass")
    access_token = create_access_token(data={"sub": user.username},)
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        user = db.query(Users).filter(Users.username == username).first()
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception


@router.get('/profile',response_model = None)
def get_user_profile(current_user: Users = Depends(get_current_user)):
    return UserSchema(
        id = current_user.id,
        username=current_user.username,
        email=current_user.email,
        password = current_user.password
    )