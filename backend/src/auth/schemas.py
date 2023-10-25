from typing import Union, List, Optional

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    password: str
    class Config():
        from_attributes =True


class TitleSchema(BaseModel):
   id: int
   title: str

class LoginSchema(BaseModel):
   id: int
   title: str   


class Token(BaseModel):
    access_token: str
    token_type: str
    