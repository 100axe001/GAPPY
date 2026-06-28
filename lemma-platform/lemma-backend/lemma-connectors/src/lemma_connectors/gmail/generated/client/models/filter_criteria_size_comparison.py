from enum import Enum

class FilterCriteriaSizeComparison(str, Enum):
    LARGER = "larger"
    SMALLER = "smaller"
    UNSPECIFIED = "unspecified"

    def __str__(self) -> str:
        return str(self.value)
