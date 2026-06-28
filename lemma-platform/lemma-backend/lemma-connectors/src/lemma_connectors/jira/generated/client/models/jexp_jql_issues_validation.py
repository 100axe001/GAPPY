from enum import Enum

class JexpJqlIssuesValidation(str, Enum):
    NONE = "none"
    STRICT = "strict"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
