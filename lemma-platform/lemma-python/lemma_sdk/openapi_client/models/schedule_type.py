from enum import Enum


class ScheduleType(str, Enum):
    DATASTORE = "DATASTORE"
    TIME = "TIME"
    WEBHOOK = "WEBHOOK"

    def __str__(self) -> str:
        return str(self.value)
