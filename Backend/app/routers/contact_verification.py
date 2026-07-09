from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.contact_verification import (
    SendOTP,
    VerifyOTP,
    ContactVerificationResponse
)
from app.services.contact_verification_service import (
    send_otp,
    verify_otp
)

router = APIRouter(
    prefix="/contact-verification",
    tags=["Contact Verification"]
)


@router.post("/send-otp", response_model=ContactVerificationResponse)
def send_otp_api(data: SendOTP, db: Session = Depends(get_db)):
    return send_otp(data, db)


@router.post("/verify-otp")
def verify_otp_api(data: VerifyOTP, db: Session = Depends(get_db)):
    return verify_otp(data, db)