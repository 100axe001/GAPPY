from enum import Enum

class FindUsersAndGroupsAvatarSize(str, Enum):
    LARGE = "large"
    LARGE2X = "large@2x"
    LARGE3X = "large@3x"
    MEDIUM = "medium"
    MEDIUM2X = "medium@2x"
    MEDIUM3X = "medium@3x"
    SMALL = "small"
    SMALL2X = "small@2x"
    SMALL3X = "small@3x"
    XLARGE = "xlarge"
    XLARGE2X = "xlarge@2x"
    XLARGE3X = "xlarge@3x"
    XSMALL = "xsmall"
    XSMALL2X = "xsmall@2x"
    XSMALL3X = "xsmall@3x"
    XXLARGE = "xxlarge"
    XXLARGE2X = "xxlarge@2x"
    XXLARGE3X = "xxlarge@3x"
    XXXLARGE = "xxxlarge"
    XXXLARGE2X = "xxxlarge@2x"
    XXXLARGE3X = "xxxlarge@3x"

    def __str__(self) -> str:
        return str(self.value)
