from sqlalchemy.orm import Session
from app.models.society import Society
from app.schemas.society import SocietyCreate


def create_society(db: Session, society: SocietyCreate):
    db_society = Society(
        society_name=society.society_name,
        address=society.address
    )

    db.add(db_society)
    db.commit()
    db.refresh(db_society)
    return db_society


def get_all_societies(db: Session):
    return db.query(Society).all()


def get_society_by_id(db: Session, society_id: int):
    return db.query(Society).filter(Society.id == society_id).first()