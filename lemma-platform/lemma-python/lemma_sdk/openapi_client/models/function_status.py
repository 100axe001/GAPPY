from enum import Enum


class FunctionStatus(str, Enum):
    CODE_GENERATION = "CODE_GENERATION"
    DRAFT = "DRAFT"
    ERROR = "ERROR"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
