from enum import Enum

class IssueFieldOptionConfigurationAttributesItem(str, Enum):
    DEFAULTVALUE = "defaultValue"
    NOTSELECTABLE = "notSelectable"

    def __str__(self) -> str:
        return str(self.value)
