from enum import Enum

class ScorecardChartSpecNumberFormatSource(str, Enum):
    CHART_NUMBER_FORMAT_SOURCE_UNDEFINED = "CHART_NUMBER_FORMAT_SOURCE_UNDEFINED"
    CUSTOM = "CUSTOM"
    FROM_DATA = "FROM_DATA"

    def __str__(self) -> str:
        return str(self.value)
