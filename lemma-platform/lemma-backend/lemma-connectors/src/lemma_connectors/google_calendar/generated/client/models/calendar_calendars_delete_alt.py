from enum import Enum

class CalendarCalendarsDeleteAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
