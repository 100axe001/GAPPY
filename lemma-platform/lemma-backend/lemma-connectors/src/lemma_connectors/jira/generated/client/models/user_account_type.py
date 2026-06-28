from enum import Enum

class UserAccountType(str, Enum):
    APP = "app"
    ATLASSIAN = "atlassian"
    CUSTOMER = "customer"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
