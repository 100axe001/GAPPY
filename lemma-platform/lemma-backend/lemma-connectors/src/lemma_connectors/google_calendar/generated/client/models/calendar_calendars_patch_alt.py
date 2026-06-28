from enum import Enum

class CalendarCalendarsPatchAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
