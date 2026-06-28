from enum import Enum

class DeleteWorkflowTransitionPropertyWorkflowMode(str, Enum):
    DRAFT = "draft"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
