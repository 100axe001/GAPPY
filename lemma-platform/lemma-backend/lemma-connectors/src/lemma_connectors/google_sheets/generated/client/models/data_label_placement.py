from enum import Enum

class DataLabelPlacement(str, Enum):
    ABOVE = "ABOVE"
    BELOW = "BELOW"
    CENTER = "CENTER"
    DATA_LABEL_PLACEMENT_UNSPECIFIED = "DATA_LABEL_PLACEMENT_UNSPECIFIED"
    INSIDE_BASE = "INSIDE_BASE"
    INSIDE_END = "INSIDE_END"
    LEFT = "LEFT"
    OUTSIDE_END = "OUTSIDE_END"
    RIGHT = "RIGHT"

    def __str__(self) -> str:
        return str(self.value)
