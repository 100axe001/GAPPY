from enum import Enum

class CellFormatWrapStrategy(str, Enum):
    CLIP = "CLIP"
    LEGACY_WRAP = "LEGACY_WRAP"
    OVERFLOW_CELL = "OVERFLOW_CELL"
    WRAP = "WRAP"
    WRAP_STRATEGY_UNSPECIFIED = "WRAP_STRATEGY_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
