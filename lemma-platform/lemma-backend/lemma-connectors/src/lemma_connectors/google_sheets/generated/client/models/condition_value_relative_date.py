from enum import Enum

class ConditionValueRelativeDate(str, Enum):
    PAST_MONTH = "PAST_MONTH"
    PAST_WEEK = "PAST_WEEK"
    PAST_YEAR = "PAST_YEAR"
    RELATIVE_DATE_UNSPECIFIED = "RELATIVE_DATE_UNSPECIFIED"
    TODAY = "TODAY"
    TOMORROW = "TOMORROW"
    YESTERDAY = "YESTERDAY"

    def __str__(self) -> str:
        return str(self.value)
