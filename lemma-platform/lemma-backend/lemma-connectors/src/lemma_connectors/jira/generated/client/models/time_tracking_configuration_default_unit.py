from enum import Enum

class TimeTrackingConfigurationDefaultUnit(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
