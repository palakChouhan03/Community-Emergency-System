from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name:str
    email:EmailStr 
    phone:str
    password:str 
    role: str='Resident'

class UserLogin(BaseModel):
    email: EmailStr
    password: str 

class AssignFlat(BaseModel):
    flat_id: int    