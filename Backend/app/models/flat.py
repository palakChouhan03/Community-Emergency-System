from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base
from sqlalchemy.orm import relationship


class Flat(Base):
    __tablename__ = "flats"

    id = Column(Integer, primary_key=True, index=True)
    flat_number = Column(String(20), nullable=False)
    residents = relationship("User", back_populates="flat")

    block_id = Column(Integer, ForeignKey("blocks.id"))