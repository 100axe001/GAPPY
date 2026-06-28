from enum import Enum

class TextToColumnsRequestDelimiterType(str, Enum):
    AUTODETECT = "AUTODETECT"
    COMMA = "COMMA"
    CUSTOM = "CUSTOM"
    DELIMITER_TYPE_UNSPECIFIED = "DELIMITER_TYPE_UNSPECIFIED"
    PERIOD = "PERIOD"
    SEMICOLON = "SEMICOLON"
    SPACE = "SPACE"

    def __str__(self) -> str:
        return str(self.value)
