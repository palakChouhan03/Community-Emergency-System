from fastapi import FastAPI
from app.models.role import Role
from app.models.user import User
from app.models.society import Society
from app.models.block import Block
from app.models.flat import Flat
from app.models.emergency_contact import EmergencyContact
from app.database.connection import engine, Base
from app.routers.user import router as user_router
from app.routers.society import router as society_router
from app.models.role import Role
from app.routers.role import router as role_router
from app.models.block import Block
from app.routers.block import router as block_router
from app.models.flat import Flat
from app.routers.flat import router as flat_router
from app.models.emergency_contact import EmergencyContact
from app.routers.emergency_contact import router as emergency_contact_router
from app.models.contact_verification import ContactVerification
from app.models.contact_verification import ContactVerification
from app.routers.contact_verification import router as contact_verification_router
from app.routers import emergency

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Community Emergency Coordination System",
    version="1.0.0"
)
app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Community Emergency Coordination System"
    }

app.include_router(society_router)
app.include_router(role_router)
app.include_router(block_router)
app.include_router(flat_router)
app.include_router(emergency_contact_router)
app.include_router(contact_verification_router)
app.include_router(emergency.router)