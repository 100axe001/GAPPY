from enum import Enum

class LicensedApplicationPlan(str, Enum):
    FREE = "FREE"
    PAID = "PAID"
    UNLICENSED = "UNLICENSED"

    def __str__(self) -> str:
        return str(self.value)
