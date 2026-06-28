from enum import Enum

class SheetsSpreadsheetsValuesAppendValueInputOption(str, Enum):
    INPUT_VALUE_OPTION_UNSPECIFIED = "INPUT_VALUE_OPTION_UNSPECIFIED"
    RAW = "RAW"
    USER_ENTERED = "USER_ENTERED"

    def __str__(self) -> str:
        return str(self.value)
