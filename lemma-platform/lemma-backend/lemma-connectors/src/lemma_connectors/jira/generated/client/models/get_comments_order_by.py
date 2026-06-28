from enum import Enum

class GetCommentsOrderBy(str, Enum):
    CREATED = "created"
    VALUE_1 = "-created"
    VALUE_2 = "+created"

    def __str__(self) -> str:
        return str(self.value)
