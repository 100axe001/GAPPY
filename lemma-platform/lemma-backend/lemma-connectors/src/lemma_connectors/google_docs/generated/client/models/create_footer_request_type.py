from enum import Enum

class CreateFooterRequestType(str, Enum):
    DEFAULT = "DEFAULT"
    HEADER_FOOTER_TYPE_UNSPECIFIED = "HEADER_FOOTER_TYPE_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
