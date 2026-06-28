from enum import Enum

class SharePermissionInputBeanType(str, Enum):
    AUTHENTICATED = "authenticated"
    GLOBAL = "global"
    GROUP = "group"
    PROJECT = "project"
    PROJECTROLE = "projectRole"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
