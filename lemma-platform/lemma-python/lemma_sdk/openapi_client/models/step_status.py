from enum import Enum


class StepStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
