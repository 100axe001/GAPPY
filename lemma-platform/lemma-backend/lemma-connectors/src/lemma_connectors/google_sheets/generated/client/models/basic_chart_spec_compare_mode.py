from enum import Enum

class BasicChartSpecCompareMode(str, Enum):
    BASIC_CHART_COMPARE_MODE_UNSPECIFIED = "BASIC_CHART_COMPARE_MODE_UNSPECIFIED"
    CATEGORY = "CATEGORY"
    DATUM = "DATUM"

    def __str__(self) -> str:
        return str(self.value)
