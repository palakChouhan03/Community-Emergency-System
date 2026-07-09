from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import require_role
from app.models.user import User
from app.database.session import get_db
from app.schemas.flat import FlatCreate
from app.services.flat_service import (
    create_flat,
    get_all_flats,
    get_flat_by_id
)

router = APIRouter(
    prefix="/flat",
    tags=["Flat"]
)

@router.post("/create")
def add_flat(
    flat: FlatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(2))
):
    return create_flat(db, flat)

@router.get("/")
def get_flats(db: Session = Depends(get_db)):
    return get_all_flats(db)

@router.get("/{flat_id}")
def get_flat(flat_id: int, db: Session = Depends(get_db)):
    flat = get_flat_by_id(db, flat_id)

    if not flat:
        raise HTTPException(status_code=404, detail="Flat not found")

    return flat