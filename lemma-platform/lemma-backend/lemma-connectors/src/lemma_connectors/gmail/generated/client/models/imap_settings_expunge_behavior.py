from enum import Enum

class ImapSettingsExpungeBehavior(str, Enum):
    ARCHIVE = "archive"
    DELETEFOREVER = "deleteForever"
    EXPUNGEBEHAVIORUNSPECIFIED = "expungeBehaviorUnspecified"
    TRASH = "trash"

    def __str__(self) -> str:
        return str(self.value)
