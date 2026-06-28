from enum import Enum

class FieldChangedClauseOperator(str, Enum):
    CHANGED = "changed"

    def __str__(self) -> str:
        return str(self.value)
