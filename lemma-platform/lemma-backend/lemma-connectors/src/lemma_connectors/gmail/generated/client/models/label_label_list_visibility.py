from enum import Enum

class LabelLabelListVisibility(str, Enum):
    LABELHIDE = "labelHide"
    LABELSHOW = "labelShow"
    LABELSHOWIFUNREAD = "labelShowIfUnread"

    def __str__(self) -> str:
        return str(self.value)
