from enum import Enum

class SearchForIssuesUsingJqlValidateQuery(str, Enum):
    FALSE = "false"
    NONE = "none"
    STRICT = "strict"
    TRUE = "true"
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
