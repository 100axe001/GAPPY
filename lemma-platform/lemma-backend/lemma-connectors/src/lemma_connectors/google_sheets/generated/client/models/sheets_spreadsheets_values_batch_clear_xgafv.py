from enum import Enum

class SheetsSpreadsheetsValuesBatchClearXgafv(str, Enum):
    VALUE_0 = "1"
    VALUE_1 = "2"

    def __str__(self) -> str:
        return str(self.value)
