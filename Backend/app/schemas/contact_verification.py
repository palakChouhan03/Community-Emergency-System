from pydantic import BaseModel
from datetime import datetime


class SendOTP(BaseModel):
    phone: str


class VerifyOTP(BaseModel):
    phone: str
    otp: str


class ContactVerificationResponse(BaseModel):
    id: int
    phone: str
    otp: str
    is_verified: bool
    expires_at: datetime | None
    created_at: datetime

    class Config:
        from_attributes = True