from enum import Enum

class GroupLabelType(str, Enum):
    ADMIN = "ADMIN"
    MULTIPLE = "MULTIPLE"
    SINGLE = "SINGLE"

    def __str__(self) -> str:
        return str(self.value)
