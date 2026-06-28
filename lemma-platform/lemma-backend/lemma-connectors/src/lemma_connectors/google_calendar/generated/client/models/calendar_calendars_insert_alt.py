from enum import Enum

class CalendarCalendarsInsertAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
