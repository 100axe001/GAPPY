from enum import Enum

class GetWorkflowsPaginatedOrderBy(str, Enum):
    CREATED = "created"
    NAME = "name"
    UPDATED = "updated"
    VALUE_1 = "-name"
    VALUE_2 = "+name"
    VALUE_4 = "-created"
    VALUE_5 = "+created"
    VALUE_7 = "+updated"
    VALUE_8 = "-updated"

    def __str__(self) -> str:
        return str(self.value)
