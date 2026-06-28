from enum import Enum

class JiraExpressionValidationErrorType(str, Enum):
    OTHER = "other"
    SYNTAX = "syntax"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
