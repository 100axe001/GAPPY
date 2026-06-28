from enum import Enum

class GetScreensOrderBy(str, Enum):
    ID = "id"
    NAME = "name"
    VALUE_1 = "-name"
    VALUE_2 = "+name"
    VALUE_4 = "-id"
    VALUE_5 = "+id"

    def __str__(self) -> str:
        return str(self.value)
