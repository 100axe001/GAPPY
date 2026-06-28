from enum import Enum

class AutoForwardingDisposition(str, Enum):
    ARCHIVE = "archive"
    DISPOSITIONUNSPECIFIED = "dispositionUnspecified"
    LEAVEININBOX = "leaveInInbox"
    MARKREAD = "markRead"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
