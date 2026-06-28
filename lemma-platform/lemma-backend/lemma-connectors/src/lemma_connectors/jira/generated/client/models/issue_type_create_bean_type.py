from enum import Enum

class IssueTypeCreateBeanType(str, Enum):
    STANDARD = "standard"
    SUBTASK = "subtask"

    def __str__(self) -> str:
        return str(self.value)
