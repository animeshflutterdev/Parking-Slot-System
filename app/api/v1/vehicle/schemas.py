from pydantic import BaseModel, Field
from datetime import datetime

from app.api.v1.vehicle.constants import VehicleType, VehiclePlateColorType

class CreateVehicleSchema(BaseModel):

    plate_number: str = Field(min_length=10)
    plate_color: VehiclePlateColorType
    description: str | None = None
    vehicle_type: VehicleType

class VehicleResponseSchema(BaseModel):

    id: str
    plate_number: str = Field(min_length=10)
    plate_color: VehiclePlateColorType
    description: str | None = None
    vehicle_type: VehicleType
    created_at: datetime

    class Config:
        from_attributes = True

class GetVehicle(BaseModel):
    plate_number: str | None = None