from enum import Enum

class DriveCommentsCreateAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
