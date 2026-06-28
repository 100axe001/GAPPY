from enum import Enum

class GetAvatarImageByOwnerFormat(str, Enum):
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
