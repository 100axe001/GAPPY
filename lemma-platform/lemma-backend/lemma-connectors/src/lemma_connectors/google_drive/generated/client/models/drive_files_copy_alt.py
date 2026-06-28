from enum import Enum

class DriveFilesCopyAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
