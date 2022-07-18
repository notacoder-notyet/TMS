import email
from lib2to3.pgen2 import token
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class Login(BaseModel):
    email: EmailStr
    password: str