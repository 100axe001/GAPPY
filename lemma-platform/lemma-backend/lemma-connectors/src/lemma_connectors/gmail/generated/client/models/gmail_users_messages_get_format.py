from enum import Enum

class GmailUsersMessagesGetFormat(str, Enum):
    FULL = "full"
    METADATA = "metadata"
    MINIMAL = "minimal"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
