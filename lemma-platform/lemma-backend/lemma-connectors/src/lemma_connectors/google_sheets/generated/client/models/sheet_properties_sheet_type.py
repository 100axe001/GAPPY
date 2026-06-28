from enum import Enum

class SheetPropertiesSheetType(str, Enum):
    DATA_SOURCE = "DATA_SOURCE"
    GRID = "GRID"
    OBJECT = "OBJECT"
    SHEET_TYPE_UNSPECIFIED = "SHEET_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
