from enum import Enum

class NestingLevelBulletAlignment(str, Enum):
    BULLET_ALIGNMENT_UNSPECIFIED = "BULLET_ALIGNMENT_UNSPECIFIED"
    CENTER = "CENTER"
    END = "END"
    START = "START"

    def __str__(self) -> str:
        return str(self.value)
