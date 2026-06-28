from enum import Enum

class CopyPasteRequestPasteOrientation(str, Enum):
    NORMAL = "NORMAL"
    TRANSPOSE = "TRANSPOSE"

    def __str__(self) -> str:
        return str(self.value)
