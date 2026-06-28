from enum import Enum

class DateTimeRuleType(str, Enum):
    DATE_TIME_RULE_TYPE_UNSPECIFIED = "DATE_TIME_RULE_TYPE_UNSPECIFIED"
    DAY_MONTH = "DAY_MONTH"
    DAY_OF_MONTH = "DAY_OF_MONTH"
    DAY_OF_WEEK = "DAY_OF_WEEK"
    DAY_OF_YEAR = "DAY_OF_YEAR"
    HOUR = "HOUR"
    HOUR_MINUTE = "HOUR_MINUTE"
    HOUR_MINUTE_AMPM = "HOUR_MINUTE_AMPM"
    MINUTE = "MINUTE"
    MONTH = "MONTH"
    QUARTER = "QUARTER"
    SECOND = "SECOND"
    YEAR = "YEAR"
    YEAR_MONTH = "YEAR_MONTH"
    YEAR_MONTH_DAY = "YEAR_MONTH_DAY"
    YEAR_QUARTER = "YEAR_QUARTER"

    def __str__(self) -> str:
        return str(self.value)
