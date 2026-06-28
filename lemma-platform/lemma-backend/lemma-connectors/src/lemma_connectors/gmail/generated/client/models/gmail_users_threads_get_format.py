from enum import Enum

class GmailUsersThreadsGetFormat(str, Enum):
    FULL = "full"
    METADATA = "metadata"
    MINIMAL = "minimal"

    def __str__(self) -> str:
        return str(self.value)
