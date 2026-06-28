from enum import Enum

class CseKeyPairEnablementState(str, Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    STATEUNSPECIFIED = "stateUnspecified"

    def __str__(self) -> str:
        return str(self.value)
