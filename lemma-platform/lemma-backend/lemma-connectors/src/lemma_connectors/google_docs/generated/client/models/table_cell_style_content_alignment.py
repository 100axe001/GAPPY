from enum import Enum

class TableCellStyleContentAlignment(str, Enum):
    BOTTOM = "BOTTOM"
    CONTENT_ALIGNMENT_UNSPECIFIED = "CONTENT_ALIGNMENT_UNSPECIFIED"
    CONTENT_ALIGNMENT_UNSUPPORTED = "CONTENT_ALIGNMENT_UNSUPPORTED"
    MIDDLE = "MIDDLE"
    TOP = "TOP"

    def __str__(self) -> str:
        return str(self.value)
