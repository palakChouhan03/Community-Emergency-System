from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):

    existing_role = db.query(Role).filter(
        Role.role_name == role.role_name
    ).first()

    if existing_role:
        return existing_role

    db_role = Role(role_name=role.role_name)

    db.add(db_role)
    db.commit()
    db.refresh(db_role)

    return db_role

def get_all_roles(db: Session):
    return db.query(Role).all()


def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()