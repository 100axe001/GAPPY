from enum import Enum

class ParagraphStyleAlignment(str, Enum):
    ALIGNMENT_UNSPECIFIED = "ALIGNMENT_UNSPECIFIED"
    CENTER = "CENTER"
    END = "END"
    JUSTIFIED = "JUSTIFIED"
    START = "START"

    def __str__(self) -> str:
        return str(self.value)
