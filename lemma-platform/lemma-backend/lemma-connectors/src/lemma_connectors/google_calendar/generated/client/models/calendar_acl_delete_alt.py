from enum import Enum

class CalendarAclDeleteAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
