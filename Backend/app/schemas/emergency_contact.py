from pydantic import BaseModel

class EmergencyContactCreate(BaseModel):
    contact_name: str
    phone: str
    relation: str
    user_id: int


class EmergencyContactResponse(EmergencyContactCreate):
    id: int
    is_verified: bool

    class Config:
        from_attributes = True