from enum import Enum

class FieldLastUsedType(str, Enum):
    NOT_TRACKED = "NOT_TRACKED"
    NO_INFORMATION = "NO_INFORMATION"
    TRACKED = "TRACKED"

    def __str__(self) -> str:
        return str(self.value)
