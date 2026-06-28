from enum import Enum

class JqlQueryClauseTimePredicateOperator(str, Enum):
    AFTER = "after"
    BEFORE = "before"
    BY = "by"
    DURING = "during"
    FROM = "from"
    ON = "on"
    TO = "to"

    def __str__(self) -> str:
        return str(self.value)
