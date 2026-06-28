from enum import Enum

class MergeCellsRequestMergeType(str, Enum):
    MERGE_ALL = "MERGE_ALL"
    MERGE_COLUMNS = "MERGE_COLUMNS"
    MERGE_ROWS = "MERGE_ROWS"

    def __str__(self) -> str:
        return str(self.value)
