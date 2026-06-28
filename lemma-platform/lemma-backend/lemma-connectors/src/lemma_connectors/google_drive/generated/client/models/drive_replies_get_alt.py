from enum import Enum

class DriveRepliesGetAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
