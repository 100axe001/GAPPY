from enum import Enum

class GetScreensScopeItem(str, Enum):
    GLOBAL = "GLOBAL"
    PROJECT = "PROJECT"
    TEMPLATE = "TEMPLATE"

    def __str__(self) -> str:
        return str(self.value)
