from enum import Enum

class DeleteWorklogAdjustEstimate(str, Enum):
    AUTO = "auto"
    LEAVE = "leave"
    MANUAL = "manual"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
