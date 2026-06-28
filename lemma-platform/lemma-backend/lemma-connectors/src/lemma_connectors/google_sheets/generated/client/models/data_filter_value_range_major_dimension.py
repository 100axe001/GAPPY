from enum import Enum

class DataFilterValueRangeMajorDimension(str, Enum):
    COLUMNS = "COLUMNS"
    DIMENSION_UNSPECIFIED = "DIMENSION_UNSPECIFIED"
    ROWS = "ROWS"

    def __str__(self) -> str:
        return str(self.value)
