from enum import Enum

class StatusCreateStatusCategory(str, Enum):
    DONE = "DONE"
    IN_PROGRESS = "IN_PROGRESS"
    TODO = "TODO"

    def __str__(self) -> str:
        return str(self.value)
