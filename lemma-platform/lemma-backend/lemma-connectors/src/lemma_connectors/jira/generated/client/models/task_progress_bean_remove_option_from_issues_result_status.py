from enum import Enum

class TaskProgressBeanRemoveOptionFromIssuesResultStatus(str, Enum):
    CANCELLED = "CANCELLED"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    COMPLETE = "COMPLETE"
    DEAD = "DEAD"
    ENQUEUED = "ENQUEUED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
