from enum import Enum


class WorkflowRunWaitType(str, Enum):
    AGENT = "AGENT"
    FUNCTION = "FUNCTION"
    HUMAN = "HUMAN"
    TIME = "TIME"

    def __str__(self) -> str:
        return str(self.value)
