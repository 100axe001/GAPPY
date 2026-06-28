from enum import Enum

class TextStyleBaselineOffset(str, Enum):
    BASELINE_OFFSET_UNSPECIFIED = "BASELINE_OFFSET_UNSPECIFIED"
    NONE = "NONE"
    SUBSCRIPT = "SUBSCRIPT"
    SUPERSCRIPT = "SUPERSCRIPT"

    def __str__(self) -> str:
        return str(self.value)
