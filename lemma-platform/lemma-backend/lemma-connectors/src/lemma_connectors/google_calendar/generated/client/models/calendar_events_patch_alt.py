from enum import Enum

class CalendarEventsPatchAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
