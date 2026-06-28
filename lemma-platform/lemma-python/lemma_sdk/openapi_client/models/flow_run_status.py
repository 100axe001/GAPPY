from enum import Enum


class FlowRunStatus(str, Enum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
