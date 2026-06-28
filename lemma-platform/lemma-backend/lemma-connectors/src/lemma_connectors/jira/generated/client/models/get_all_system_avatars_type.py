from enum import Enum

class GetAllSystemAvatarsType(str, Enum):
    ISSUETYPE = "issuetype"
    PROJECT = "project"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
