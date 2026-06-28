from enum import Enum

class ParseJqlQueriesValidation(str, Enum):
    NONE = "none"
    STRICT = "strict"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
