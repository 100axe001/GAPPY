from enum import Enum


class RecordAccessMode(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
