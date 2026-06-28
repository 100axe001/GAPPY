from enum import Enum


class ConversationType(str, Enum):
    CHAT = "CHAT"
    PROJECT = "PROJECT"
    TASK = "TASK"

    def __str__(self) -> str:
        return str(self.value)
