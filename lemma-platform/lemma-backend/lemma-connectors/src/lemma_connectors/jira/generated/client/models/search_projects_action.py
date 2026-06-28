from enum import Enum

class SearchProjectsAction(str, Enum):
    BROWSE = "browse"
    EDIT = "edit"
    VIEW = "view"

    def __str__(self) -> str:
        return str(self.value)
