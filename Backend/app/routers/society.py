from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.society import SocietyCreate, SocietyResponse
from app.database.session import get_db
from app.schemas.society import SocietyCreate
from app.services.society_service import (
    create_society,
    get_all_societies,
    get_society_by_id,
)

router = APIRouter(
    prefix="/society",
    tags=["Society"]
)


@router.post("/create", response_model=SocietyResponse)
def add_society(society: SocietyCreate, db: Session = Depends(get_db)):
    return create_society(db, society)


@router.get("/", response_model=List[SocietyResponse])
def get_societies(db: Session = Depends(get_db)):
    return get_all_societies(db)

@router.get("/{society_id}", response_model=SocietyResponse)
def get_society(society_id: int, db: Session = Depends(get_db)):
    society = get_society_by_id(db, society_id)

    if not society:
        raise HTTPException(
            status_code=404,
            detail="Society not found"
        )

    return society