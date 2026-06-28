from enum import Enum


class DatastoreOperation(str, Enum):
    DELETE = "DELETE"
    INSERT = "INSERT"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
