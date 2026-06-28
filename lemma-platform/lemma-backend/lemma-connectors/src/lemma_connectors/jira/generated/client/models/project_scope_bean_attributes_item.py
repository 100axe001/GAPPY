from enum import Enum

class ProjectScopeBeanAttributesItem(str, Enum):
    DEFAULTVALUE = "defaultValue"
    NOTSELECTABLE = "notSelectable"

    def __str__(self) -> str:
        return str(self.value)
