from enum import Enum

class ThemeColorPairColorType(str, Enum):
    ACCENT1 = "ACCENT1"
    ACCENT2 = "ACCENT2"
    ACCENT3 = "ACCENT3"
    ACCENT4 = "ACCENT4"
    ACCENT5 = "ACCENT5"
    ACCENT6 = "ACCENT6"
    BACKGROUND = "BACKGROUND"
    LINK = "LINK"
    TEXT = "TEXT"
    THEME_COLOR_TYPE_UNSPECIFIED = "THEME_COLOR_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
