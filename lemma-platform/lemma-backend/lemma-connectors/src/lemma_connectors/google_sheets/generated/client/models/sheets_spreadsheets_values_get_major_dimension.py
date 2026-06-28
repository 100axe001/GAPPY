from enum import Enum

class SheetsSpreadsheetsValuesGetMajorDimension(str, Enum):
    COLUMNS = "COLUMNS"
    DIMENSION_UNSPECIFIED = "DIMENSION_UNSPECIFIED"
    ROWS = "ROWS"

    def __str__(self) -> str:
        return str(self.value)
