from enum import Enum

class DataLabelType(str, Enum):
    CUSTOM = "CUSTOM"
    DATA = "DATA"
    DATA_LABEL_TYPE_UNSPECIFIED = "DATA_LABEL_TYPE_UNSPECIFIED"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
