from enum import Enum


class PodRole(str, Enum):
    POD_ADMIN = "POD_ADMIN"
    POD_EDITOR = "POD_EDITOR"
    POD_USER = "POD_USER"
    POD_VIEWER = "POD_VIEWER"

    def __str__(self) -> str:
        return str(self.value)
