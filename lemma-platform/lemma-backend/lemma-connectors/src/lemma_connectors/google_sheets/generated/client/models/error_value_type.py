from enum import Enum

class ErrorValueType(str, Enum):
    DIVIDE_BY_ZERO = "DIVIDE_BY_ZERO"
    ERROR = "ERROR"
    ERROR_TYPE_UNSPECIFIED = "ERROR_TYPE_UNSPECIFIED"
    LOADING = "LOADING"
    NAME = "NAME"
    NULL_VALUE = "NULL_VALUE"
    NUM = "NUM"
    N_A = "N_A"
    REF = "REF"
    VALUE = "VALUE"

    def __str__(self) -> str:
        return str(self.value)
