from enum import Enum

class DriveDrivesUnhideAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
