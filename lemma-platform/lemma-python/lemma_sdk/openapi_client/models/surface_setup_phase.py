from enum import Enum


class SurfaceSetupPhase(str, Enum):
    CONFIGURE_PROVIDER = "CONFIGURE_PROVIDER"
    CREATE_SURFACE = "CREATE_SURFACE"
    PREPARE = "PREPARE"
    VERIFY = "VERIFY"

    def __str__(self) -> str:
        return str(self.value)
