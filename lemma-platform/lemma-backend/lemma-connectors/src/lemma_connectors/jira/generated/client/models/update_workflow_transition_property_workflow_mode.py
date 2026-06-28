from enum import Enum

class UpdateWorkflowTransitionPropertyWorkflowMode(str, Enum):
    DRAFT = "draft"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
