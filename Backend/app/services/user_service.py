from sqlalchemy.orm import Session
from app.models.user import User
from app.models.society import Society
from app.models.role import Role
from app.schemas.user import AssignFlat
from app.schemas.user import UserCreate, UserLogin, AssignFlat
from app.core.security import create_access_token
from app.core.security import hash_password, verify_password


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):

    role = db.query(Role).filter(Role.role_name == user.role).first()

    society = db.query(Society).first()   # First society (id = 1)

    db_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hash_password(user.password),
        role_id=role.id,
        society_id=society.id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
    "id": db_user.id,
    "full_name": db_user.full_name,
    "email": db_user.email,
    "phone": db_user.phone,
    "role_id": db_user.role_id,
    "society_id": db_user.society_id,
    "flat_id": db_user.flat_id,
    "is_verified": db_user.is_verified
}

def login_user(db: Session, user: UserLogin):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return None

    if not verify_password(user.password, db_user.password):
        return None
    
    if not db_user.is_verified:
        return {"message": "Please verify your phone number first"}

    token = create_access_token(
    {
        "sub": db_user.email,
        "role": db_user.role_id
    }
)

    return {
    "message": "Login Successful",
    "access_token": token,
    "token_type": "bearer",
    "user": {
        "id": db_user.id,
        "full_name": db_user.full_name,
        "email": db_user.email,
        "phone": db_user.phone,
        "role_id": db_user.role_id,
        "society_id": db_user.society_id,
        "flat_id": db_user.flat_id,
        "is_verified": db_user.is_verified
    }
}


def get_all_users(db: Session):
    return db.query(User).all()

def assign_flat(db: Session, user_id: int, flat_data: AssignFlat):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    user.flat_id = flat_data.flat_id

    db.commit()
    db.refresh(user)

    return user