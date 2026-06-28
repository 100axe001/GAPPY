from enum import Enum

class GmailUsersMessagesInsertInternalDateSource(str, Enum):
    DATEHEADER = "dateHeader"
    RECEIVEDTIME = "receivedTime"

    def __str__(self) -> str:
        return str(self.value)
