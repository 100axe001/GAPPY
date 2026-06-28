from enum import Enum

class DriveCommentsListAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
