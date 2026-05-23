from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.api.v1.vehicle.schemas import (
    CreateVehicleSchema,
    GetVehicle
)

from app.api.v1.vehicle.service import (
    VehicleService
)

router = APIRouter()


@router.post("/")
def create_vehicle(payload: CreateVehicleSchema, db: Session = Depends(get_db)):
    service = VehicleService(db)
    return service.create_vehicle(payload)

@router.get('/get')
def get_vehicle(plate_number: str, db: Session = Depends(get_db)):
    service = VehicleService(db)
    return service.get_vehicle(plate_number)

@router.get('/all')
def get_vehicle(db: Session = Depends(get_db)):
    service = VehicleService(db)
    return service.get_all_vehicle()