from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: str
    password: str
    profile_photo: str = None  


class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    profile_photo: Optional[str] = None  
