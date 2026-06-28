from enum import Enum

class ReplaceImageRequestImageReplaceMethod(str, Enum):
    CENTER_CROP = "CENTER_CROP"
    IMAGE_REPLACE_METHOD_UNSPECIFIED = "IMAGE_REPLACE_METHOD_UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
