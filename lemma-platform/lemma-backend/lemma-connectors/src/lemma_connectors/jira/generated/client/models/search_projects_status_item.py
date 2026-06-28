from enum import Enum

class SearchProjectsStatusItem(str, Enum):
    ARCHIVED = "archived"
    DELETED = "deleted"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
