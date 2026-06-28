from enum import Enum

class SlicerSpecHorizontalAlignment(str, Enum):
    CENTER = "CENTER"
    HORIZONTAL_ALIGN_UNSPECIFIED = "HORIZONTAL_ALIGN_UNSPECIFIED"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
