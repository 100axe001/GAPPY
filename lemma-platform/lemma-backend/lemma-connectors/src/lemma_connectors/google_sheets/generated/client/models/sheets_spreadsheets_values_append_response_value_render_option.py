from enum import Enum

class SheetsSpreadsheetsValuesAppendResponseValueRenderOption(str, Enum):
    FORMATTED_VALUE = "FORMATTED_VALUE"
    FORMULA = "FORMULA"
    UNFORMATTED_VALUE = "UNFORMATTED_VALUE"

    def __str__(self) -> str:
        return str(self.value)
