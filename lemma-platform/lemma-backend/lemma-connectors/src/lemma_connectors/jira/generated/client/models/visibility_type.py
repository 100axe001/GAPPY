from enum import Enum

class VisibilityType(str, Enum):
    GROUP = "group"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
