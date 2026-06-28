from enum import Enum

class GetFieldsPaginatedOrderBy(str, Enum):
    CONTEXTSCOUNT = "contextsCount"
    LASTUSED = "lastUsed"
    NAME = "name"
    PROJECTSCOUNT = "projectsCount"
    SCREENSCOUNT = "screensCount"
    VALUE_1 = "-contextsCount"
    VALUE_10 = "-screensCount"
    VALUE_11 = "+screensCount"
    VALUE_13 = "-projectsCount"
    VALUE_14 = "+projectsCount"
    VALUE_2 = "+contextsCount"
    VALUE_4 = "-lastUsed"
    VALUE_5 = "+lastUsed"
    VALUE_7 = "-name"
    VALUE_8 = "+name"

    def __str__(self) -> str:
        return str(self.value)
