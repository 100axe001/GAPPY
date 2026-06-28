from enum import Enum

class BasicChartSpecStackedType(str, Enum):
    BASIC_CHART_STACKED_TYPE_UNSPECIFIED = "BASIC_CHART_STACKED_TYPE_UNSPECIFIED"
    NOT_STACKED = "NOT_STACKED"
    PERCENT_STACKED = "PERCENT_STACKED"
    STACKED = "STACKED"

    def __str__(self) -> str:
        return str(self.value)
