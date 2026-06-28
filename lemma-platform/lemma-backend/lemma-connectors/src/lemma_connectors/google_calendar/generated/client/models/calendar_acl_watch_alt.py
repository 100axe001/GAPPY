from enum import Enum

class CalendarAclWatchAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
