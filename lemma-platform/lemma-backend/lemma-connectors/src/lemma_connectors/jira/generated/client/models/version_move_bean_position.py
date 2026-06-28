from enum import Enum

class VersionMoveBeanPosition(str, Enum):
    EARLIER = "Earlier"
    FIRST = "First"
    LAST = "Last"
    LATER = "Later"

    def __str__(self) -> str:
        return str(self.value)
