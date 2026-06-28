from enum import Enum

class TimeTrackingConfigurationTimeFormat(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    PRETTY = "pretty"

    def __str__(self) -> str:
        return str(self.value)
