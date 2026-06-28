from enum import Enum

class GetDashboardsPaginatedOrderBy(str, Enum):
    DESCRIPTION = "description"
    FAVORITE_COUNT = "favorite_count"
    ID = "id"
    IS_FAVORITE = "is_favorite"
    NAME = "name"
    OWNER = "owner"
    VALUE_1 = "-description"
    VALUE_10 = "-is_favorite"
    VALUE_11 = "+is_favorite"
    VALUE_13 = "-name"
    VALUE_14 = "+name"
    VALUE_16 = "-owner"
    VALUE_17 = "+owner"
    VALUE_2 = "+description"
    VALUE_4 = "-favorite_count"
    VALUE_5 = "+favorite_count"
    VALUE_7 = "-id"
    VALUE_8 = "+id"

    def __str__(self) -> str:
        return str(self.value)
