from enum import Enum

class AnalyseExpressionCheck(str, Enum):
    COMPLEXITY = "complexity"
    SYNTAX = "syntax"
    TYPE = "type"

    def __str__(self) -> str:
        return str(self.value)
