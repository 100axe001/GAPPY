from enum import Enum

class CalendarEventsWatchOrderBy(str, Enum):
    STARTTIME = "startTime"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
