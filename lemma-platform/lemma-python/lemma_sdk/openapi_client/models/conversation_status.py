from enum import Enum


class ConversationStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    STOP_REQUESTED = "STOP_REQUESTED"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
