from enum import Enum

class BorderStyle(str, Enum):
    DASHED = "DASHED"
    DOTTED = "DOTTED"
    DOUBLE = "DOUBLE"
    NONE = "NONE"
    SOLID = "SOLID"
    SOLID_MEDIUM = "SOLID_MEDIUM"
    SOLID_THICK = "SOLID_THICK"
    STYLE_UNSPECIFIED = "STYLE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
