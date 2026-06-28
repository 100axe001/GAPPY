from enum import Enum

class GetProjectVersionsPaginatedOrderBy(str, Enum):
    DESCRIPTION = "description"
    NAME = "name"
    RELEASEDATE = "releaseDate"
    SEQUENCE = "sequence"
    STARTDATE = "startDate"
    VALUE_1 = "-description"
    VALUE_10 = "-sequence"
    VALUE_11 = "+sequence"
    VALUE_13 = "-startDate"
    VALUE_14 = "+startDate"
    VALUE_2 = "+description"
    VALUE_4 = "-name"
    VALUE_5 = "+name"
    VALUE_7 = "-releaseDate"
    VALUE_8 = "+releaseDate"

    def __str__(self) -> str:
        return str(self.value)
