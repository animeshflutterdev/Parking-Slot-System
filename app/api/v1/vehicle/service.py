from fastapi import HTTPException
from app.api.v1.vehicle.repository import (
    VehicleRepository
)
from app.core.base_service import BaseService
from app.utils.helpers import Helpers


class VehicleService(BaseService):

    # def __init__(self, db):
    #     self.vehicle_repository = (
    #         VehicleRepository(db)
    #     )
    def __init__(self, db):
        super().__init__(db)
        self.vehicle_repository = (
            VehicleRepository(self.db)
        )

    # def create_vehicle(self, vehicle_data):
    #     try:
    #         existing_vehicle = (
    #             self.vehicle_repository
    #             .get_vehicle_by_plate_number(
    #                 vehicle_data.plate_number
    #             )
    #         )
    #         if existing_vehicle:
    #             raise HTTPException(
    #                 status_code=400,
    #                 detail="Vehicle already exists"
    #             )
    #         return self.vehicle_repository.create_vehicle(
    #             vehicle_data.model_dump()
    #         )
    #     except HTTPException:
    #         raise
    #     except Exception as e:
    #         log.error(
    #             message="create_vehicle_error",
    #             data={"error": str(e)},
    #             fileName="create_vehicle_error"
    #         )
    #         raise

    # def get_vehicle(self, plate_number):
    #     try:
    #         existing_vehicle = (
    #             self.vehicle_repository
    #             .get_vehicle_by_plate_number(
    #                 plate_number,
    #             )
    #         )
    #         if not existing_vehicle:
    #             raise HTTPException(
    #                 status_code=400,
    #                 detail="No vehicle found"
    #             )
    #         return existing_vehicle
    #     except HTTPException:
    #         raise
    #     except Exception as e:
    #         log.error(
    #             message="get_vehicle_error",
    #             data={"error": str(e)},
    #             fileName="get_vehicle_error"
    #         )
    #         raise


    @Helpers.handle_service_exception("create_vehicle")
    def create_vehicle(self, vehicle_data):

        existing_vehicle = (
            self.vehicle_repository
            .get_vehicle_by_plate_number(
                vehicle_data.plate_number
            )
        )

        if existing_vehicle:
            raise HTTPException(
                status_code=400,
                detail="Vehicle already exists"
            )

        return self.vehicle_repository.create_vehicle(
            vehicle_data.model_dump()
        )


    @Helpers.handle_service_exception("get_vehicle")
    def get_vehicle(self, plate_number):

        existing_vehicle = (
            self.vehicle_repository
            .get_vehicle_by_plate_number(
                plate_number,
            )
        )

        if not existing_vehicle:
            raise HTTPException(
                status_code=404,
                detail="No vehicle found"
            )

        return existing_vehicle


    @Helpers.handle_service_exception("get_all_vehicle")
    def get_all_vehicle(self):
        all_vehicle = (self.vehicle_repository.get_all_vehicle())

        if len(all_vehicle) <= 0:
            raise HTTPException(
                status_code=404,
                detail="No vehicle found"
            )

        return all_vehicle
