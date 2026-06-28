from enum import Enum

class DriveDrivesListAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
