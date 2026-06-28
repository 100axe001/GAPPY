from enum import Enum

class OrgChartSpecNodeSize(str, Enum):
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    ORG_CHART_LABEL_SIZE_UNSPECIFIED = "ORG_CHART_LABEL_SIZE_UNSPECIFIED"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
