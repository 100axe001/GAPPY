from enum import Enum

class DimensionUnit(str, Enum):
    PT = "PT"
    UNIT_UNSPECIFIED = "UNIT_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
