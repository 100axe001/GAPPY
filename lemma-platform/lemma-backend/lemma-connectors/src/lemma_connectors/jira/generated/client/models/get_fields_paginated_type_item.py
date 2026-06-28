from enum import Enum

class GetFieldsPaginatedTypeItem(str, Enum):
    CUSTOM = "custom"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
