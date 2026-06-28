from enum import Enum

class ScopeType(str, Enum):
    PROJECT = "PROJECT"
    TEMPLATE = "TEMPLATE"

    def __str__(self) -> str:
        return str(self.value)
