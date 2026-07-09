from sqlalchemy.orm import Session

from app.models.emergency import Emergency


def create_emergency(db: Session, emergency, user_id: int):

    db_emergency = Emergency(
        title=emergency.title,
        description=emergency.description,
        emergency_type=emergency.emergency_type,
        user_id=user_id
    )

    db.add(db_emergency)
    db.commit()
    db.refresh(db_emergency)

    return db_emergency

def get_all_emergencies(db:Session):
    return db.query(Emergency).all()

def update_emergency(db: Session, emergency_id: int, status: str):
    emergency = db.query(Emergency).filter(
        Emergency.id == emergency_id
    ).first()

    if not emergency:
        return None

    emergency.status = status

    db.commit()
    db.refresh(emergency)

    return emergency

def get_emergency_by_id(db: Session, emergency_id: int):
    return db.query(Emergency).filter(
        Emergency.id == emergency_id).first()

def delete_emergency(db: Session, emergency_id: int):
    emergency = db.query(Emergency).filter(
        Emergency.id == emergency_id
    ).first()

    if not emergency:
        return None

    db.delete(emergency)
    db.commit()

    return {
        "message": "Emergency deleted successfully"
    }