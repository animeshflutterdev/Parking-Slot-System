from pydantic import BaseModel
from datetime import datetime

from app.api.v1.parking_slot.constants import (
    SlotType
)


class CreateParkingSlotSchema(BaseModel):

    slot_number: str
    slot_type: SlotType
    floor: str
    # is_occupied is not accepted from the client — new slots are always free.


class ParkingSlotResponseSchema(BaseModel):

    id: str
    slot_number: str
    slot_type: SlotType
    floor: str
    is_occupied: bool
    vehicle_id: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class ParkVehicleSchema(BaseModel):
    """Input for POST /park — pick a free slot for this vehicle."""
    plate_number: str
    slot_type: SlotType


class ParkResponseSchema(BaseModel):
    slot_id: str
    slot_number: str
    floor: str
    slot_type: SlotType
    vehicle_id: str
    plate_number: str

    class Config:
        from_attributes = True
