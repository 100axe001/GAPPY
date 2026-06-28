from enum import Enum

class SortSpecSortOrder(str, Enum):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"
    SORT_ORDER_UNSPECIFIED = "SORT_ORDER_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
