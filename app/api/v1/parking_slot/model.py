from sqlalchemy import (Column,String,Boolean,DateTime,ForeignKey)

from app.core.database import Base

from datetime import datetime
import uuid


class ParkingSlot(Base):

    __tablename__ = "parking_slots"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    slot_number = Column(
        String,
        unique=True,
        nullable=False
    )

    slot_type = Column(
        String,
        nullable=False
    )

    floor = Column(
        String,
        nullable=False
    )

    is_occupied = Column(
        Boolean,
        default=False,
        nullable=False
    )

    # Which vehicle currently occupies this slot. NULL when free.
    vehicle_id = Column(
        String,
        ForeignKey("vehicles.id"),
        nullable=True
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