from enum import Enum

class EmbeddedObjectBorderPropertyState(str, Enum):
    NOT_RENDERED = "NOT_RENDERED"
    RENDERED = "RENDERED"

    def __str__(self) -> str:
        return str(self.value)
