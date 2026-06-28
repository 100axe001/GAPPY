from enum import Enum

class CalendarEventsInsertSendUpdates(str, Enum):
    ALL = "all"
    EXTERNALONLY = "externalOnly"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
