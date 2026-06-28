from enum import Enum

class KeywordOperandKeyword(str, Enum):
    EMPTY = "empty"

    def __str__(self) -> str:
        return str(self.value)
