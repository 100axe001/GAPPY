from enum import Enum

class ParagraphStyleNamedStyleType(str, Enum):
    HEADING_1 = "HEADING_1"
    HEADING_2 = "HEADING_2"
    HEADING_3 = "HEADING_3"
    HEADING_4 = "HEADING_4"
    HEADING_5 = "HEADING_5"
    HEADING_6 = "HEADING_6"
    NAMED_STYLE_TYPE_UNSPECIFIED = "NAMED_STYLE_TYPE_UNSPECIFIED"
    NORMAL_TEXT = "NORMAL_TEXT"
    SUBTITLE = "SUBTITLE"
    TITLE = "TITLE"

    def __str__(self) -> str:
        return str(self.value)
