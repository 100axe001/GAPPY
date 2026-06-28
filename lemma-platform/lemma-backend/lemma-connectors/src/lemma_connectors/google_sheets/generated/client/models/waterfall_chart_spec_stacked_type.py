from enum import Enum

class WaterfallChartSpecStackedType(str, Enum):
    SEQUENTIAL = "SEQUENTIAL"
    STACKED = "STACKED"
    WATERFALL_STACKED_TYPE_UNSPECIFIED = "WATERFALL_STACKED_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
