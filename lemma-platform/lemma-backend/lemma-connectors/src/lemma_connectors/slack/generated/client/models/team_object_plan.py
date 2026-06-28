from enum import Enum

class TeamObjectPlan(str, Enum):
    COMPLIANCE = "compliance"
    ENTERPRISE = "enterprise"
    PLUS = "plus"
    STD = "std"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
