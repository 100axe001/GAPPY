from enum import Enum

class ProjectStyle(str, Enum):
    CLASSIC = "classic"
    NEXT_GEN = "next-gen"

    def __str__(self) -> str:
        return str(self.value)
