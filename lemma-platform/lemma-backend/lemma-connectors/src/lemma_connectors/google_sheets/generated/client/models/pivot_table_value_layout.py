from enum import Enum

class PivotTableValueLayout(str, Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"

    def __str__(self) -> str:
        return str(self.value)
