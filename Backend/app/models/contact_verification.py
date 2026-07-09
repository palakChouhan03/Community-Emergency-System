from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.connection import Base


class ContactVerification(Base):
    __tablename__ = "contact_verifications"

    id = Column(Integer, primary_key=True, index=True)

    phone = Column(String(15), nullable=False)

    otp = Column(String(6), nullable=False)

    is_verified = Column(Boolean, default=False)

    expires_at = Column(DateTime)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )