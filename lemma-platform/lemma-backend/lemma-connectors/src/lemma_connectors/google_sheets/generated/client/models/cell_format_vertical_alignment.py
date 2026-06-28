from enum import Enum

class CellFormatVerticalAlignment(str, Enum):
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    TOP = "TOP"
    VERTICAL_ALIGN_UNSPECIFIED = "VERTICAL_ALIGN_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
