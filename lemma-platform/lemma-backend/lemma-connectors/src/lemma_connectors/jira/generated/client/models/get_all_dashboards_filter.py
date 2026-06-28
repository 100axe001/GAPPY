from enum import Enum

class GetAllDashboardsFilter(str, Enum):
    FAVOURITE = "favourite"
    MY = "my"

    def __str__(self) -> str:
        return str(self.value)
