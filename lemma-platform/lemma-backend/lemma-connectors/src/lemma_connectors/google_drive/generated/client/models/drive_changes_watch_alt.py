from enum import Enum

class DriveChangesWatchAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
