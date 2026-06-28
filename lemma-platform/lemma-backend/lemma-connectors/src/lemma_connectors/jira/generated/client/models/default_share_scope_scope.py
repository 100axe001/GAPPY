from enum import Enum

class DefaultShareScopeScope(str, Enum):
    AUTHENTICATED = "AUTHENTICATED"
    GLOBAL = "GLOBAL"
    PRIVATE = "PRIVATE"

    def __str__(self) -> str:
        return str(self.value)
