from enum import Enum

class NumberFormatType(str, Enum):
    CURRENCY = "CURRENCY"
    DATE = "DATE"
    DATE_TIME = "DATE_TIME"
    NUMBER = "NUMBER"
    NUMBER_FORMAT_TYPE_UNSPECIFIED = "NUMBER_FORMAT_TYPE_UNSPECIFIED"
    PERCENT = "PERCENT"
    SCIENTIFIC = "SCIENTIFIC"
    TEXT = "TEXT"
    TIME = "TIME"

    def __str__(self) -> str:
        return str(self.value)
