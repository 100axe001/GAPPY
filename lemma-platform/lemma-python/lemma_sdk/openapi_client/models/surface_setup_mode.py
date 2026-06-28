from enum import Enum


class SurfaceSetupMode(str, Enum):
    CONNECTED_ACCOUNT = "CONNECTED_ACCOUNT"
    PLATFORM_BUILT_IN = "PLATFORM_BUILT_IN"

    def __str__(self) -> str:
        return str(self.value)
