from sqlalchemy.orm import Session

from app.api.v1.parking_slot.model import (
    ParkingSlot
)


class ParkingSlotRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_slot(self, slot_data):
        slot = ParkingSlot(**slot_data)
        self.db.add(slot)
        self.db.commit()
        self.db.refresh(slot)
        return slot
    
    def get_available_slot(self,slot_type: str):
        return (
            self.db.query(ParkingSlot)
            .filter(
                ParkingSlot.slot_type == slot_type,
                ParkingSlot.is_occupied == False
            )
            .first()
        )
    
    def occupy_slot(self, slot):
        slot.is_occupied = True
        self.db.commit()
        self.db.refresh(slot)
        return slot
    
    def release_slot(self, slot):
        slot.is_occupied = False
        self.db.commit()
        self.db.refresh(slot)
        return slot
    
    def get_all_slots(self):
        return ( self.db.query(ParkingSlot).all() )
    
    