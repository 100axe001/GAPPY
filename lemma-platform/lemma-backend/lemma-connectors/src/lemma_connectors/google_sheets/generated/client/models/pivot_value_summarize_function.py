from enum import Enum

class PivotValueSummarizeFunction(str, Enum):
    AVERAGE = "AVERAGE"
    COUNT = "COUNT"
    COUNTA = "COUNTA"
    COUNTUNIQUE = "COUNTUNIQUE"
    CUSTOM = "CUSTOM"
    MAX = "MAX"
    MEDIAN = "MEDIAN"
    MIN = "MIN"
    PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED = "PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED"
    PRODUCT = "PRODUCT"
    STDEV = "STDEV"
    STDEVP = "STDEVP"
    SUM = "SUM"
    VAR = "VAR"
    VARP = "VARP"

    def __str__(self) -> str:
        return str(self.value)
