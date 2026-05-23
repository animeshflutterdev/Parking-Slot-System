from app.core.base_service import BaseService
from app.api.v1.parking_slot.repository import (ParkingSlotRepository)
from app.utils.helpers import Helpers

class ParkingSlotService(BaseService):

    def __init__(self, db):
        super().__init__(db)
        self.slot_repository = (
            ParkingSlotRepository(self.db)
        )

    @Helpers.handle_service_exception("create_slot")
    def create_slot(self, payload):
        return (
            self.slot_repository.create_slot(
                payload.model_dump()
            )
        )

    @Helpers.handle_service_exception("get_available_slot")
    def get_available_slot(self, slot_type):
        return ( self.slot_repository.get_available_slot(slot_type) )

    @Helpers.handle_service_exception("occupy_slot")
    def occupy_slot(self, slot):
        return ( self.slot_repository.occupy_slot(slot) )

    @Helpers.handle_service_exception("release_slot")
    def release_slot(self, slot):
        return ( self.slot_repository.release_slot(slot) )

    # @Helpers.handle_service_exception("release_slot")
    # def release_slot(self, slot):
    #     return ( self.slot_repository.release_slot(slot) )

    @Helpers.handle_service_exception("get_all_slots")
    def get_all_slots(self):
        return ( self.slot_repository.get_all_slots() )