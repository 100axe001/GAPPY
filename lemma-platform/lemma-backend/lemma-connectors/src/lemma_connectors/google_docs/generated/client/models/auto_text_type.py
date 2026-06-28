from enum import Enum

class AutoTextType(str, Enum):
    PAGE_COUNT = "PAGE_COUNT"
    PAGE_NUMBER = "PAGE_NUMBER"
    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
