from enum import Enum

class ProjectFeatureStateState(str, Enum):
    COMING_SOON = "COMING_SOON"
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"

    def __str__(self) -> str:
        return str(self.value)
