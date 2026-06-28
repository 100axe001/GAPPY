from enum import Enum

class InsertSectionBreakRequestSectionType(str, Enum):
    CONTINUOUS = "CONTINUOUS"
    NEXT_PAGE = "NEXT_PAGE"
    SECTION_TYPE_UNSPECIFIED = "SECTION_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
