from enum import Enum


class FunctionType(str, Enum):
    API = "API"
    JOB = "JOB"

    def __str__(self) -> str:
        return str(self.value)
