from pydantic import BaseModel
from datetime import datetime
from typing import Optional




class EmergencyCreate(BaseModel):
    title: str
    description: str
    emergency_type: str
    status: str
    user_id: int
    created_at:datetime

class EmergencyResponse(BaseModel):
    id: int
    title: str
    description: str
    emergency_type: str
    status: str
    user_id: int
    created_at: datetime  

    class Config:
        from_attributes= True

class EmergencyUpdate(BaseModel):
    status: Optional[str] = None