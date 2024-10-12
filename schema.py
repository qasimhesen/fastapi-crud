from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username:str
    password: str
    class Config:
        extra = "forbid"



class UserDeleteSchema(BaseModel):
    username: str
    
    class Config:
        extra = "forbid"



class UserGetSchema(BaseModel):
    username: str
    
    class Config:
        extra = "forbid"


class UserUpdateSchema(BaseModel):
    password:str
    new_password:str
    class Config:
        extra="forbid"


class Reset_All_Base(BaseModel):
    username:str
    password:str
    class Confif:
        extra = "forbid"



