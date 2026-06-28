from enum import Enum

class FieldValueClauseOperator(str, Enum):
    IN = "in"
    IS = "is"
    IS_NOT = "is not"
    NOT_IN = "not in"
    VALUE_0 = "="
    VALUE_1 = "!="
    VALUE_2 = ">"
    VALUE_3 = "<"
    VALUE_4 = ">="
    VALUE_5 = "<="
    VALUE_8 = "~"
    VALUE_9 = "~="

    def __str__(self) -> str:
        return str(self.value)
