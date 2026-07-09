from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship

from app.database.connection import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_verified = Column(Boolean,default=False)

    role_id = Column(Integer, ForeignKey("roles.id"))
    society_id = Column(Integer, ForeignKey("societies.id"))
    flat_id = Column(Integer, ForeignKey("flats.id"))

    role = relationship("Role")
    society = relationship("Society")
    flat = relationship("Flat", back_populates="residents")
    
    