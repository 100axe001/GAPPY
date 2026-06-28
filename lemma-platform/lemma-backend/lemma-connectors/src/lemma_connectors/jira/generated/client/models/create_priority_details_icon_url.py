from enum import Enum

class CreatePriorityDetailsIconUrl(str, Enum):
    VALUE_0 = "/images/icons/priorities/blocker.png"
    VALUE_1 = "/images/icons/priorities/critical.png"
    VALUE_2 = "/images/icons/priorities/high.png"
    VALUE_3 = "/images/icons/priorities/highest.png"
    VALUE_4 = "/images/icons/priorities/low.png"
    VALUE_5 = "/images/icons/priorities/lowest.png"
    VALUE_6 = "/images/icons/priorities/major.png"
    VALUE_7 = "/images/icons/priorities/medium.png"
    VALUE_8 = "/images/icons/priorities/minor.png"
    VALUE_9 = "/images/icons/priorities/trivial.png"

    def __str__(self) -> str:
        return str(self.value)
