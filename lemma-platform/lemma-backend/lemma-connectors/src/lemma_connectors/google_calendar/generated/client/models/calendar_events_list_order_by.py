from enum import Enum

class CalendarEventsListOrderBy(str, Enum):
    STARTTIME = "startTime"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
