from enum import Enum


class WorkflowMode(str, Enum):
    GLOBAL = "GLOBAL"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
