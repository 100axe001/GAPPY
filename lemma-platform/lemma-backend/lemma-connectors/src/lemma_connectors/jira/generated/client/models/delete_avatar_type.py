from enum import Enum

class DeleteAvatarType(str, Enum):
    ISSUETYPE = "issuetype"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
