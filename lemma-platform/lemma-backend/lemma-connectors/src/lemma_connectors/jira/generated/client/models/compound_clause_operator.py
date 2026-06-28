from enum import Enum

class CompoundClauseOperator(str, Enum):
    AND = "and"
    NOT = "not"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
