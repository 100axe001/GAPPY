from enum import Enum

class GetFiltersPaginatedOrderBy(str, Enum):
    DESCRIPTION = "description"
    FAVOURITE_COUNT = "favourite_count"
    ID = "id"
    IS_FAVOURITE = "is_favourite"
    IS_SHARED = "is_shared"
    NAME = "name"
    OWNER = "owner"
    VALUE_1 = "-description"
    VALUE_10 = "-is_favourite"
    VALUE_11 = "+is_favourite"
    VALUE_13 = "-name"
    VALUE_14 = "+name"
    VALUE_16 = "-owner"
    VALUE_17 = "+owner"
    VALUE_19 = "-is_shared"
    VALUE_2 = "+description"
    VALUE_20 = "+is_shared"
    VALUE_4 = "-favourite_count"
    VALUE_5 = "+favourite_count"
    VALUE_7 = "-id"
    VALUE_8 = "+id"

    def __str__(self) -> str:
        return str(self.value)
