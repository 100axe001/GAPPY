from enum import Enum

class ScorecardChartSpecAggregateType(str, Enum):
    AVERAGE = "AVERAGE"
    CHART_AGGREGATE_TYPE_UNSPECIFIED = "CHART_AGGREGATE_TYPE_UNSPECIFIED"
    COUNT = "COUNT"
    MAX = "MAX"
    MEDIAN = "MEDIAN"
    MIN = "MIN"
    SUM = "SUM"

    def __str__(self) -> str:
        return str(self.value)
