from enum import Enum

class SpreadsheetPropertiesAutoRecalc(str, Enum):
    HOUR = "HOUR"
    MINUTE = "MINUTE"
    ON_CHANGE = "ON_CHANGE"
    RECALCULATION_INTERVAL_UNSPECIFIED = "RECALCULATION_INTERVAL_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
