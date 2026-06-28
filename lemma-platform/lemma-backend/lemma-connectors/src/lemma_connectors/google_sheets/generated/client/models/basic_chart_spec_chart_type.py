from enum import Enum

class BasicChartSpecChartType(str, Enum):
    AREA = "AREA"
    BAR = "BAR"
    BASIC_CHART_TYPE_UNSPECIFIED = "BASIC_CHART_TYPE_UNSPECIFIED"
    COLUMN = "COLUMN"
    COMBO = "COMBO"
    LINE = "LINE"
    SCATTER = "SCATTER"
    STEPPED_AREA = "STEPPED_AREA"

    def __str__(self) -> str:
        return str(self.value)
