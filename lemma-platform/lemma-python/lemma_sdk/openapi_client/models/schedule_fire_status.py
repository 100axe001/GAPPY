from enum import Enum


class ScheduleFireStatus(str, Enum):
    ERROR = "ERROR"
    FILTERED = "FILTERED"
    TRIGGERED = "TRIGGERED"

    def __str__(self) -> str:
        return str(self.value)
