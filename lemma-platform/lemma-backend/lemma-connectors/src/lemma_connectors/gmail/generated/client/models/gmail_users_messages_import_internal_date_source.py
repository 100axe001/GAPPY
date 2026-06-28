from enum import Enum

class GmailUsersMessagesImportInternalDateSource(str, Enum):
    DATEHEADER = "dateHeader"
    RECEIVEDTIME = "receivedTime"

    def __str__(self) -> str:
        return str(self.value)
