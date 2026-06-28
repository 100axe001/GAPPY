from enum import Enum

class GmailUsersSettingsSendAsUpdateAlt(str, Enum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def __str__(self) -> str:
        return str(self.value)
