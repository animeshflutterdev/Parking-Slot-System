from pydantic import BaseModel
from datetime import datetime

from app.api.v1.parking_slot.constants import (
    SlotType
)


class CreateParkingSlotSchema(BaseModel):

    slot_number: str
    slot_type: SlotType
    floor: str
    is_occupied: bool


class ParkingSlotResponseSchema(BaseModel):

    id: str
    slot_number: str
    slot_type: SlotType
    is_occupied: bool
    created_at: datetime

    class Config:
        from_attributes = True