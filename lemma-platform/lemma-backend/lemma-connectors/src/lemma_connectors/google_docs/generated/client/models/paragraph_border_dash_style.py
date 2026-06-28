from enum import Enum

class ParagraphBorderDashStyle(str, Enum):
    DASH = "DASH"
    DASH_STYLE_UNSPECIFIED = "DASH_STYLE_UNSPECIFIED"
    DOT = "DOT"
    SOLID = "SOLID"

    def __str__(self) -> str:
        return str(self.value)
