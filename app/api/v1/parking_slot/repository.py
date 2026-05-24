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

    def get_available_slot(self, slot_type: str):
        return (
            self.db.query(ParkingSlot)
            .filter(
                ParkingSlot.slot_type == slot_type,
                ParkingSlot.is_occupied == False
            )
            .first()
        )

    def get_slot_by_id(self, slot_id: str):
        return (
            self.db.query(ParkingSlot)
            .filter(ParkingSlot.id == slot_id)
            .first()
        )

    def try_occupy_slot(self, slot_id: str, vehicle_id: str) -> bool:
        """
        Atomically claim a slot for a vehicle.

        Issues a single UPDATE ... WHERE id=? AND is_occupied=False
        so two concurrent requests cannot both succeed on the same row.

        Returns True if this caller claimed the slot, False if it was
        already taken by someone else.
        """
        rows_updated = (
            self.db.query(ParkingSlot)
            .filter(
                ParkingSlot.id == slot_id,
                ParkingSlot.is_occupied == False,
            )
            .update(
                {
                    "is_occupied": True,
                    "vehicle_id": vehicle_id,
                },
                synchronize_session=False,
            )
        )
        self.db.commit()
        return rows_updated > 0

    def release_slot(self, slot_id: str) -> bool:
        """
        Atomically free a slot. Returns True if this call actually
        released an occupied slot, False if it was already free.
        """
        rows_updated = (
            self.db.query(ParkingSlot)
            .filter(
                ParkingSlot.id == slot_id,
                ParkingSlot.is_occupied == True,
            )
            .update(
                {
                    "is_occupied": False,
                    "vehicle_id": None,
                },
                synchronize_session=False,
            )
        )
        self.db.commit()
        return rows_updated > 0

    def get_all_slots(self):
        return self.db.query(ParkingSlot).all()
