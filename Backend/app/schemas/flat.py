from pydantic import BaseModel

class FlatCreate(BaseModel):
    flat_number: str
    block_id: int

class FlatResponse(FlatCreate):
    id: int

    class Config:
        from_attributes = True