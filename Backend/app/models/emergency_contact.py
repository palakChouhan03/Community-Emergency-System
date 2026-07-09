from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.connection import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True, index=True)

    contact_name = Column(String(100), nullable=False)

    phone = Column(String(15), nullable=False)

    relation = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())