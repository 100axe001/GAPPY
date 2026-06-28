from enum import Enum

class SharePermissionType(str, Enum):
    AUTHENTICATED = "authenticated"
    GLOBAL = "global"
    GROUP = "group"
    LOGGEDIN = "loggedin"
    PROJECT = "project"
    PROJECTROLE = "projectRole"
    PROJECT_UNKNOWN = "project-unknown"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
