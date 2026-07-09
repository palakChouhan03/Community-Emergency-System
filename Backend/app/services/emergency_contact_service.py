from sqlalchemy.orm import Session

from app.models.emergency_contact import EmergencyContact


def create_emergency_contact(db: Session, contact):
    db_contact = EmergencyContact(**contact.dict())

    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    return db_contact


def get_all_contacts(db: Session):
    return db.query(EmergencyContact).all()


def get_contact_by_id(db: Session, contact_id: int):
    return db.query(EmergencyContact).filter(
        EmergencyContact.id == contact_id
    ).first()


def update_contact(db: Session, contact_id: int, contact):

    db_contact = db.query(EmergencyContact).filter(
        EmergencyContact.id == contact_id
    ).first()

    if not db_contact:
        return None

    db_contact.contact_name = contact.contact_name
    db_contact.phone = contact.phone
    db_contact.relation = contact.relation
    db_contact.user_id = contact.user_id

    db.commit()
    db.refresh(db_contact)

    return db_contact


def delete_contact(db: Session, contact_id: int):

    db_contact = db.query(EmergencyContact).filter(
        EmergencyContact.id == contact_id
    ).first()

    if not db_contact:
        return None

    db.delete(db_contact)
    db.commit()

    return {"message": "Emergency Contact Deleted Successfully"}