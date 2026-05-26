from app.core.logger import log
from functools import wraps
from fastapi import HTTPException
from app.core.logger import log

class Helpers:
    def handle_service_exception_bkp(operation_name: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except HTTPException:
                    raise
                except Exception as e:
                    log.error(
                        message=f"{operation_name}_error",
                        data={"error": str(e)},
                        fileName=f"{operation_name}_error"
                    )
                    raise HTTPException(
                        status_code=500,
                        detail="Internal Server Error"
                    )

            return wrapper

        return decorator
    
    def check_vehicle_number(plate_number: str) -> bool:
        plate_number = plate_number.replace(" ", "")
        if len(plate_number) > 10 or len(plate_number) < 0:
            return False
        return True
    
    @staticmethod
    def handle_service_exception(operation_name: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except HTTPException as e:
                    log.error(
                        message=f"{operation_name}_error_1",
                        data={"error": str(e)},
                        fileName=f"{operation_name}_error_1"
                    )
                    raise e

                except Exception as e:
                    log.error(
                        message=f"{operation_name}_error",
                        data={"error": str(e)},
                        fileName=f"{operation_name}_error"
                    )
                    raise HTTPException(
                        status_code=500,
                        detail=f"{operation_name} failed: {str(e)}"
                    )
            return wrapper
        return decorator

helper = Helpers()