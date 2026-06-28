from enum import Enum

class GetProjectTypeByKeyProjectTypeKey(str, Enum):
    BUSINESS = "business"
    PRODUCT_DISCOVERY = "product_discovery"
    SERVICE_DESK = "service_desk"
    SOFTWARE = "software"

    def __str__(self) -> str:
        return str(self.value)
