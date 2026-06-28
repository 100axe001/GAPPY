from enum import Enum


class SurfaceSetupFieldSource(str, Enum):
    CREATE_REQUEST = "CREATE_REQUEST"
    CREATE_RESPONSE = "CREATE_RESPONSE"

    def __str__(self) -> str:
        return str(self.value)
