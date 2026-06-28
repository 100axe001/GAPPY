from enum import Enum

class GetDashboardsPaginatedStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
