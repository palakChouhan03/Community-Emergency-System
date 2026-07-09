from pydantic import BaseModel

class SocietyCreate(BaseModel):
    society_name: str
    address: str

class SocietyResponse(BaseModel):
    id: int
    society_name: str
    address: str

    class Config:
        from_attributes = True