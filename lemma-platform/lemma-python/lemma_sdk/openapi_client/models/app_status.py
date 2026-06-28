from enum import Enum


class AppStatus(str, Enum):
    DRAFT = "DRAFT"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
