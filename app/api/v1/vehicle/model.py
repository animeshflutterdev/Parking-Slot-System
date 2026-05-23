from sqlalchemy import Column, String, DateTime
from app.core.database import Base
from datetime import datetime
import uuid

# CREATE TABLE vehicles (
#     id TEXT PRIMARY KEY,
#     plate_number TEXT
#     .....
# )

class Vehicle(Base):

    __tablename__ = "vehicles"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    plate_number = Column(
        String,
        unique=True,
        nullable=False
    )

    plate_color= Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    vehicle_type = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )