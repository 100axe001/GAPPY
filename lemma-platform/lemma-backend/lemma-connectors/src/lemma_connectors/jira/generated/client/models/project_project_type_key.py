from enum import Enum

class ProjectProjectTypeKey(str, Enum):
    BUSINESS = "business"
    SERVICE_DESK = "service_desk"
    SOFTWARE = "software"

    def __str__(self) -> str:
        return str(self.value)
