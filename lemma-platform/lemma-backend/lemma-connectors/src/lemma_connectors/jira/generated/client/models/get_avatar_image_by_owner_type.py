from enum import Enum

class GetAvatarImageByOwnerType(str, Enum):
    ISSUETYPE = "issuetype"
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
