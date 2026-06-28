from enum import Enum

class DriveDrivesGetAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
