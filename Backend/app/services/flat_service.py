from sqlalchemy.orm import Session
from app.models.flat import Flat

def create_flat(db: Session, flat):
    db_flat = Flat(**flat.dict())
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat

def get_all_flats(db: Session):
    return db.query(Flat).all()

def get_flat_by_id(db: Session, flat_id: int):
    return db.query(Flat).filter(Flat.id == flat_id).first()