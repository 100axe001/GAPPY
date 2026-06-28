from enum import Enum


class RuntimeProfileScope(str, Enum):
    ORGANIZATION = "ORGANIZATION"
    PERSONAL = "PERSONAL"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
