from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.emergency import EmergencyCreate, EmergencyResponse
from app.services.emergency_service import create_emergency, get_all_emergencies, get_emergency_by_id
from app.core.security import get_current_user

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency"]
)

@router.post("/")
def report_emergency(
    emergency: EmergencyCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return create_emergency(
        db,
        emergency,
        current_user.id
    )

@router.get("/", response_model=list[EmergencyResponse])
def get_emergencies(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_emergencies(db)


from app.schemas.emergency import (
    EmergencyCreate,
    EmergencyResponse,
    EmergencyUpdate
)

from app.services.emergency_service import (
    create_emergency,
    get_all_emergencies,
    update_emergency
)


@router.put("/{emergency_id}", response_model=EmergencyResponse)
def update_emergency_status(
    emergency_id: int,
    emergency: EmergencyUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    updated = update_emergency(
        db,
        emergency_id,
        emergency.status
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Emergency not found")

    return updated

@router.get("/{emergency_id}", response_model=EmergencyResponse)
def get_emergency(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    emergency = get_emergency_by_id(db, emergency_id)

    if not emergency:
        raise HTTPException(
            status_code=404,
            detail="Emergency not found"
        )

    return emergency

from app.services.emergency_service import (
    create_emergency,
    get_all_emergencies,
    update_emergency,
    get_emergency_by_id,
    delete_emergency
)

@router.delete("/{emergency_id}")
def remove_emergency(
    emergency_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    deleted = delete_emergency(db, emergency_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Emergency not found"
        )

    return deleted