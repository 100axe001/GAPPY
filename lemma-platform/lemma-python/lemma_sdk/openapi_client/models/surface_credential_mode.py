from enum import Enum


class SurfaceCredentialMode(str, Enum):
    CUSTOM = "CUSTOM"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
