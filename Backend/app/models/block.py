from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base


class Block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True)
    block_name = Column(String(100), nullable=False)

    society_id = Column(Integer, ForeignKey("societies.id"))