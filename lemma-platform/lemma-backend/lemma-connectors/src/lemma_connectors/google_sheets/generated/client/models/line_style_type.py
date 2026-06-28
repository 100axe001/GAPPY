from enum import Enum

class LineStyleType(str, Enum):
    CUSTOM = "CUSTOM"
    DOTTED = "DOTTED"
    INVISIBLE = "INVISIBLE"
    LINE_DASH_TYPE_UNSPECIFIED = "LINE_DASH_TYPE_UNSPECIFIED"
    LONG_DASHED = "LONG_DASHED"
    LONG_DASHED_DOTTED = "LONG_DASHED_DOTTED"
    MEDIUM_DASHED = "MEDIUM_DASHED"
    MEDIUM_DASHED_DOTTED = "MEDIUM_DASHED_DOTTED"
    SOLID = "SOLID"

    def __str__(self) -> str:
        return str(self.value)
