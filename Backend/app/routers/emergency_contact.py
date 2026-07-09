from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.emergency_contact import EmergencyContactCreate

from app.services.emergency_contact_service import (
    create_emergency_contact,
    get_all_contacts,
    get_contact_by_id,
    update_contact,
    delete_contact
)

router = APIRouter(
    prefix="/emergency-contact",
    tags=["Emergency Contact"]
)


@router.post("/create")
def add_contact(contact: EmergencyContactCreate, db: Session = Depends(get_db)):
    return create_emergency_contact(db, contact)


@router.get("/")
def get_contacts(db: Session = Depends(get_db)):
    return get_all_contacts(db)


@router.get("/{contact_id}")
def get_contact(contact_id: int, db: Session = Depends(get_db)):

    contact = get_contact_by_id(db, contact_id)

    if not contact:
        raise HTTPException(
            status_code=404,
            detail="Emergency Contact not found"
        )

    return contact


@router.put("/{contact_id}")
def edit_contact(contact_id: int,
                 contact: EmergencyContactCreate,
                 db: Session = Depends(get_db)):

    updated_contact = update_contact(db, contact_id, contact)

    if not updated_contact:
        raise HTTPException(
            status_code=404,
            detail="Emergency Contact not found"
        )

    return updated_contact


@router.delete("/{contact_id}")
def remove_contact(contact_id: int, db: Session = Depends(get_db)):

    deleted_contact = delete_contact(db, contact_id)

    if not deleted_contact:
        raise HTTPException(
            status_code=404,
            detail="Emergency Contact not found"
        )

    return deleted_contact