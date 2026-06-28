from enum import Enum

class TableColumnPropertiesWidthType(str, Enum):
    EVENLY_DISTRIBUTED = "EVENLY_DISTRIBUTED"
    FIXED_WIDTH = "FIXED_WIDTH"
    WIDTH_TYPE_UNSPECIFIED = "WIDTH_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
