from enum import Enum

class GetAvatarImageByIDSize(str, Enum):
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"
    XLARGE = "xlarge"
    XSMALL = "xsmall"

    def __str__(self) -> str:
        return str(self.value)
