from app.core.logger import log
from functools import wraps
from fastapi import HTTPException
from app.core.logger import log

class Helpers:
    def handle_service_exception(operation_name: str):
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

helper = Helpers()