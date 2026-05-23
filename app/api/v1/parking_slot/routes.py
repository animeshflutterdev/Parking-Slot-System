from fastapi import (APIRouter,Depends)
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.api.v1.parking_slot.schemas import (CreateParkingSlotSchema)
from app.api.v1.parking_slot.service import (ParkingSlotService)

router = APIRouter()

@router.post("/slots")
def create_slot( payload: CreateParkingSlotSchema, db: Session = Depends(get_db) ):
    service = ParkingSlotService(db)
    return service.create_slot(payload)

@router.get("/slots/{slot_type}")
def get_slot(slot_type: str, db: Session = Depends(get_db)):
    service = ParkingSlotService(db)
    return service.get_available_slot(slot_type)   