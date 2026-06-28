from enum import Enum

class GetProjectComponentsPaginatedOrderBy(str, Enum):
    DESCRIPTION = "description"
    ISSUECOUNT = "issueCount"
    LEAD = "lead"
    NAME = "name"
    VALUE_1 = "-description"
    VALUE_10 = "-name"
    VALUE_11 = "+name"
    VALUE_2 = "+description"
    VALUE_4 = "-issueCount"
    VALUE_5 = "+issueCount"
    VALUE_7 = "-lead"
    VALUE_8 = "+lead"

    def __str__(self) -> str:
        return str(self.value)
