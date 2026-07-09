from pydantic import BaseModel

class BlockCreate(BaseModel):
    block_name: str
    society_id: int

class BlockResponse(BlockCreate):
    id: int

    class Config:
        from_attributes = True