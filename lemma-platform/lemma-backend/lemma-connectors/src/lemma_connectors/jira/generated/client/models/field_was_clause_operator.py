from enum import Enum

class FieldWasClauseOperator(str, Enum):
    WAS = "was"
    WAS_IN = "was in"
    WAS_NOT = "was not"
    WAS_NOT_IN = "was not in"

    def __str__(self) -> str:
        return str(self.value)
