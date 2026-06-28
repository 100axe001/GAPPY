from enum import Enum

class ComponentWithIssueCountRealAssigneeType(str, Enum):
    COMPONENT_LEAD = "COMPONENT_LEAD"
    PROJECT_DEFAULT = "PROJECT_DEFAULT"
    PROJECT_LEAD = "PROJECT_LEAD"
    UNASSIGNED = "UNASSIGNED"

    def __str__(self) -> str:
        return str(self.value)
