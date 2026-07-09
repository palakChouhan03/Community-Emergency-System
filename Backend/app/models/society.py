from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Society(Base):
    __tablename__ = "societies"

    id = Column(Integer, primary_key=True, index=True)
    society_name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)