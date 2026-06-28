from enum import Enum

class ParagraphStyleSpacingMode(str, Enum):
    COLLAPSE_LISTS = "COLLAPSE_LISTS"
    NEVER_COLLAPSE = "NEVER_COLLAPSE"
    SPACING_MODE_UNSPECIFIED = "SPACING_MODE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
