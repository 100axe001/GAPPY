from enum import Enum

class JqlQueryFieldEntityPropertyType(str, Enum):
    DATE = "date"
    NUMBER = "number"
    STRING = "string"
    TEXT = "text"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
