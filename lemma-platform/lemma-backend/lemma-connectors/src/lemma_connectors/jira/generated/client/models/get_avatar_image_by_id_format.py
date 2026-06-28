from enum import Enum

class GetAvatarImageByIDFormat(str, Enum):
    PNG = "png"
    SVG = "svg"

    def __str__(self) -> str:
        return str(self.value)
