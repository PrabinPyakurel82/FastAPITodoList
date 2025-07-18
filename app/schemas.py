from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class TodoCreate(BaseModel):
    task: str


class TodoUpdate(BaseModel):
    task : Optional[str] = None
    completed : Optional[bool] = None

class TodoOut(BaseModel):
    id: int
    task: str
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
       from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str