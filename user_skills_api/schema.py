from pydantic import BaseModel,fields
from typing import Optional


class User(BaseModel):
    id: int
    name: str = fields.Field(max_length=10)
    age: int
    password: str
    email: str


class Skill(BaseModel):
    id:int
    name:str
    user_id:int

    class Config():
        orm_mode=True


class UpdateUsr(BaseModel):
    name: Optional[str] = fields.Field(max_length=10)
    age: Optional[int]
    email: Optional[str]


class ShowUser(BaseModel):
    id: int
    name: str
    age: int
    email: str
    skills:list

    class Config():
        orm_mode=True


class ShowSkill(BaseModel):
    name:str
    users:list

    class Config():
        orm_mode=True


class Login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None







