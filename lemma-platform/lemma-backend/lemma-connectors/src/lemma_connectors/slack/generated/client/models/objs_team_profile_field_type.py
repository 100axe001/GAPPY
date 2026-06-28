from enum import Enum

class ObjsTeamProfileFieldType(str, Enum):
    DATE = "date"
    LINK = "link"
    MAILTO = "mailto"
    OPTIONS_LIST = "options_list"
    TEXT = "text"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
