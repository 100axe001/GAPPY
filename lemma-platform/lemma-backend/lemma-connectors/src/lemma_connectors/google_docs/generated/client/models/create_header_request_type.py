from enum import Enum

class CreateHeaderRequestType(str, Enum):
    DEFAULT = "DEFAULT"
    HEADER_FOOTER_TYPE_UNSPECIFIED = "HEADER_FOOTER_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
