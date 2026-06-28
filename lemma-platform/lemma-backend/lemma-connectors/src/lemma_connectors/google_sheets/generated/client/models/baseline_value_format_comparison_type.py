from enum import Enum

class BaselineValueFormatComparisonType(str, Enum):
    ABSOLUTE_DIFFERENCE = "ABSOLUTE_DIFFERENCE"
    COMPARISON_TYPE_UNDEFINED = "COMPARISON_TYPE_UNDEFINED"
    PERCENTAGE_DIFFERENCE = "PERCENTAGE_DIFFERENCE"

    def __str__(self) -> str:
        return str(self.value)
