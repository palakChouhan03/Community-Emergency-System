from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.user import UserCreate
from app.services.user_service import create_user
from app.services.user_service import create_user, login_user, get_user_by_id
from app.schemas.user import UserCreate, UserLogin, AssignFlat
from fastapi import HTTPException

from app.services.user_service import (
    create_user,
    login_user,
    get_user_by_id,
    get_all_users,
    assign_flat
)

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = login_user(db, user)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return db_user

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user



@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.put("/assign-flat/{user_id}")
def assign_user_to_flat(
    user_id: int,
    flat: AssignFlat,
    db: Session = Depends(get_db)
):
    user = assign_flat(db, user_id, flat)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Resident assigned successfully",
        "user": user
    }