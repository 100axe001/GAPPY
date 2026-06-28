from enum import Enum

class CalendarCalendarListListMinAccessRole(str, Enum):
    FREEBUSYREADER = "freeBusyReader"
    OWNER = "owner"
    READER = "reader"
    WRITER = "writer"

    def __str__(self) -> str:
        return str(self.value)
