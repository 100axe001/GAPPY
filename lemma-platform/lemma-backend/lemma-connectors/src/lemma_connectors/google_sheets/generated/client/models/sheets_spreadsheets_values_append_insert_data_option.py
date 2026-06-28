from enum import Enum

class SheetsSpreadsheetsValuesAppendInsertDataOption(str, Enum):
    INSERT_ROWS = "INSERT_ROWS"
    OVERWRITE = "OVERWRITE"

    def __str__(self) -> str:
        return str(self.value)
