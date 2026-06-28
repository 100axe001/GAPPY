from enum import Enum

class PieChartSpecLegendPosition(str, Enum):
    BOTTOM_LEGEND = "BOTTOM_LEGEND"
    LABELED_LEGEND = "LABELED_LEGEND"
    LEFT_LEGEND = "LEFT_LEGEND"
    NO_LEGEND = "NO_LEGEND"
    PIE_CHART_LEGEND_POSITION_UNSPECIFIED = "PIE_CHART_LEGEND_POSITION_UNSPECIFIED"
    RIGHT_LEGEND = "RIGHT_LEGEND"
    TOP_LEGEND = "TOP_LEGEND"

    def __str__(self) -> str:
        return str(self.value)
