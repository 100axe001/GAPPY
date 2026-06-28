from enum import Enum

class StatusScopeType(str, Enum):
    GLOBAL = "GLOBAL"
    PROJECT = "PROJECT"

    def __str__(self) -> str:
        return str(self.value)
