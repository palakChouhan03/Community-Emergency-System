import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from app.models.user import User
from app.models.contact_verification import ContactVerification
from app.schemas.contact_verification import SendOTP, VerifyOTP


def send_otp(data: SendOTP, db: Session):

    otp = str(random.randint(100000, 999999))

    verification = ContactVerification(
        phone=data.phone,
        otp=otp,
        is_verified=False,
        expires_at=datetime.now() + timedelta(minutes=5)
    )

    db.add(verification)
    db.commit()
    db.refresh(verification)

    return verification


def verify_otp(data: VerifyOTP, db: Session):

    verification = db.query(ContactVerification).filter(
        ContactVerification.phone == data.phone,
        ContactVerification.otp == data.otp
    ).first()

    if verification is None:
        return {"message": "Invalid OTP"}

    if verification.expires_at < datetime.now():
        return {"message": "OTP Expired"}

    verification.is_verified = True

    user=db.query(User).filter(User.phone == data.phone).first()

    if user:
        user.is_verified = True


    db.commit()
    db.refresh(verification)

    return verification