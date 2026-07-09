from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import require_role
from app.database.session import get_db
from app.schemas.block import BlockCreate
from app.models.user import User
from app.services.block_service import (
    create_block,
    get_all_blocks,
    get_block_by_id
)

router = APIRouter(
    prefix="/block",
    tags=["Block"]
)

@router.post("/create")
def add_block(
    block: BlockCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(2))
):
    return create_block(db, block)

@router.get("/")
def get_blocks(db: Session = Depends(get_db)):
    return get_all_blocks(db)

@router.get("/{block_id}")
def get_block(block_id: int, db: Session = Depends(get_db)):
    block = get_block_by_id(db, block_id)

    if not block:
        raise HTTPException(status_code=404, detail="Block not found")

    return block