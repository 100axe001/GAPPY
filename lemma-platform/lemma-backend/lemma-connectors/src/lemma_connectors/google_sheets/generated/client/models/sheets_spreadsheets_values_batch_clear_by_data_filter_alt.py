from enum import Enum

class SheetsSpreadsheetsValuesBatchClearByDataFilterAlt(str, Enum):
    JSON = "json"
    MEDIA = "media"
    PROTO = "proto"

    def __str__(self) -> str:
        return str(self.value)
