from sqlalchemy.orm import Session
from app.models.block import Block
from app.schemas.block import BlockCreate

def create_block(db: Session, block: BlockCreate):
    db_block = Block(
        block_name=block.block_name,
        society_id=block.society_id
    )
    db.add(db_block)
    db.commit()
    db.refresh(db_block)
    return db_block

def get_all_blocks(db: Session):
    return db.query(Block).all()

def get_block_by_id(db: Session, block_id: int):
    return db.query(Block).filter(Block.id == block_id).first()