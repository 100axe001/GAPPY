from enum import Enum

class CalendarEventsUpdateAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
