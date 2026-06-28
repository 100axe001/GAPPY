from enum import Enum


class RuntimeProfileStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    REAUTH_REQUIRED = "REAUTH_REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
