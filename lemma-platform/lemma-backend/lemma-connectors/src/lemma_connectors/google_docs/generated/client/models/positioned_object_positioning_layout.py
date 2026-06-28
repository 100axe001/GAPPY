from enum import Enum

class PositionedObjectPositioningLayout(str, Enum):
    BEHIND_TEXT = "BEHIND_TEXT"
    BREAK_LEFT = "BREAK_LEFT"
    BREAK_LEFT_RIGHT = "BREAK_LEFT_RIGHT"
    BREAK_RIGHT = "BREAK_RIGHT"
    IN_FRONT_OF_TEXT = "IN_FRONT_OF_TEXT"
    POSITIONED_OBJECT_LAYOUT_UNSPECIFIED = "POSITIONED_OBJECT_LAYOUT_UNSPECIFIED"
    WRAP_TEXT = "WRAP_TEXT"

    def __str__(self) -> str:
        return str(self.value)
