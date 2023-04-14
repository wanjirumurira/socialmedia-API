from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
from typing import Optional

#used to create the schema of our APIS
class PostBase(BaseModel):
    title: str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    create_at: datetime
    class Config:
        orm_mode = True

class Post(PostBase):
    id : int
    create_at : datetime
    user_id : int
    owner : UserOut
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


    
