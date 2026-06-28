from enum import Enum

class SectionStyleColumnSeparatorStyle(str, Enum):
    BETWEEN_EACH_COLUMN = "BETWEEN_EACH_COLUMN"
    COLUMN_SEPARATOR_STYLE_UNSPECIFIED = "COLUMN_SEPARATOR_STYLE_UNSPECIFIED"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
