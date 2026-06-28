from enum import Enum

class JsonNodeNumberType(str, Enum):
    BIG_DECIMAL = "BIG_DECIMAL"
    BIG_INTEGER = "BIG_INTEGER"
    DOUBLE = "DOUBLE"
    FLOAT = "FLOAT"
    INT = "INT"
    LONG = "LONG"

    def __str__(self) -> str:
        return str(self.value)
