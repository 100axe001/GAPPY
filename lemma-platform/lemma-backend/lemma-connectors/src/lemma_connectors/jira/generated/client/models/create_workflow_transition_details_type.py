from enum import Enum

class CreateWorkflowTransitionDetailsType(str, Enum):
    DIRECTED = "directed"
    GLOBAL = "global"
    INITIAL = "initial"

    def __str__(self) -> str:
        return str(self.value)
