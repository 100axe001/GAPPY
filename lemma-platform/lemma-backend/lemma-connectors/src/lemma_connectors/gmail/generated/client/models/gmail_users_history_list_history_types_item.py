from enum import Enum

class GmailUsersHistoryListHistoryTypesItem(str, Enum):
    LABELADDED = "labelAdded"
    LABELREMOVED = "labelRemoved"
    MESSAGEADDED = "messageAdded"
    MESSAGEDELETED = "messageDeleted"

    def __str__(self) -> str:
        return str(self.value)
