from enum import Enum

class AddWorklogAdjustEstimate(str, Enum):
    AUTO = "auto"
    LEAVE = "leave"
    MANUAL = "manual"
    NEW = "new"

    def __str__(self) -> str:
        return str(self.value)
