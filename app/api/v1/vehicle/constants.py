from enum import Enum

class VehicleType(str, Enum):
    CAR   = "CAR"
    BIKE  = "BIKE"
    TRUCK = "TRUCK"
    AUTO  = "AUTO"

class VehiclePlateColorType(str, Enum):
    WHITE   = "WHITE"
    YELLOW  = "YELLOW"
    GREEN   = "GREEN"