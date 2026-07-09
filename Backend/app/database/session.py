from sqlalchemy.orm import sessionmaker
from app.database.connection import engine
from app.database.connection import Base
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()