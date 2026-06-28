from enum import Enum

class HistogramChartSpecLegendPosition(str, Enum):
    BOTTOM_LEGEND = "BOTTOM_LEGEND"
    HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED = "HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED"
    INSIDE_LEGEND = "INSIDE_LEGEND"
    LEFT_LEGEND = "LEFT_LEGEND"
    NO_LEGEND = "NO_LEGEND"
    RIGHT_LEGEND = "RIGHT_LEGEND"
    TOP_LEGEND = "TOP_LEGEND"

    def __str__(self) -> str:
        return str(self.value)
