from enum import Enum


class FileSearchScopeMode(str, Enum):
    DIRECT = "DIRECT"
    SUBTREE = "SUBTREE"

    def __str__(self) -> str:
        return str(self.value)
