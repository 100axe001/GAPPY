from enum import Enum

class TabStopAlignment(str, Enum):
    CENTER = "CENTER"
    END = "END"
    START = "START"
    TAB_STOP_ALIGNMENT_UNSPECIFIED = "TAB_STOP_ALIGNMENT_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
