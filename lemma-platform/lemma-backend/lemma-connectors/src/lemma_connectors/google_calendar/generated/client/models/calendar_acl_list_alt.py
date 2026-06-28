from enum import Enum

class CalendarAclListAlt(str, Enum):
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
