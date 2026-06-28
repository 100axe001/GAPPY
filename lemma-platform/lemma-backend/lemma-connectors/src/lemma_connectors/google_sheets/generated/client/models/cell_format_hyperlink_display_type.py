from enum import Enum

class CellFormatHyperlinkDisplayType(str, Enum):
    HYPERLINK_DISPLAY_TYPE_UNSPECIFIED = "HYPERLINK_DISPLAY_TYPE_UNSPECIFIED"
    LINKED = "LINKED"
    PLAIN_TEXT = "PLAIN_TEXT"

    def __str__(self) -> str:
        return str(self.value)
