from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.role import RoleCreate,RoleResponse
from typing import List
from app.core.security import require_role
from app.models.user import User
from app.services.role_service import (
    create_role,
    get_all_roles,
    get_role_by_id
)

router = APIRouter(
    prefix="/role",
    tags=["Role"]
)

@router.post("/create")
def add_role(
    role: RoleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role(1))
):
    return create_role(db, role)

@router.get("/", response_model=List[RoleResponse])
def get_roles(db: Session = Depends(get_db)):
    return get_all_roles(db)


@router.get("/{role_id}",response_model=RoleResponse)
def get_role(role_id: int, db: Session = Depends(get_db)):
    role = get_role_by_id(db, role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role

