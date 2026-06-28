from enum import Enum

class GetWorkflowTransitionRuleConfigurationsTypesItem(str, Enum):
    CONDITION = "condition"
    POSTFUNCTION = "postfunction"
    VALIDATOR = "validator"

    def __str__(self) -> str:
        return str(self.value)
