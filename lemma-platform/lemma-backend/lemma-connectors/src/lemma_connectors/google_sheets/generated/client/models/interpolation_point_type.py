from enum import Enum

class InterpolationPointType(str, Enum):
    INTERPOLATION_POINT_TYPE_UNSPECIFIED = "INTERPOLATION_POINT_TYPE_UNSPECIFIED"
    MAX = "MAX"
    MIN = "MIN"
    NUMBER = "NUMBER"
    PERCENT = "PERCENT"
    PERCENTILE = "PERCENTILE"

    def __str__(self) -> str:
        return str(self.value)
