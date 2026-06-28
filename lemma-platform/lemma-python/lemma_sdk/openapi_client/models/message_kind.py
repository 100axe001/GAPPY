from enum import Enum


class MessageKind(str, Enum):
    NOTIFICATION = "NOTIFICATION"
    TEXT = "TEXT"
    THINKING = "THINKING"
    TOOL_CALL = "TOOL_CALL"
    TOOL_RETURN = "TOOL_RETURN"

    def __str__(self) -> str:
        return str(self.value)
