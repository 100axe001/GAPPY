from enum import Enum

class CalendarEventsPatchSendUpdates(str, Enum):
    ALL = "all"
    EXTERNALONLY = "externalOnly"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
