from enum import Enum

class OrderOfIssueTypesPosition(str, Enum):
    FIRST = "First"
    LAST = "Last"

    def __str__(self) -> str:
        return str(self.value)
