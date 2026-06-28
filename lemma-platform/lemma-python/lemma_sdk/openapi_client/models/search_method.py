from enum import Enum


class SearchMethod(str, Enum):
    HYBRID = "HYBRID"
    TEXT = "TEXT"
    VECTOR = "VECTOR"

    def __str__(self) -> str:
        return str(self.value)
