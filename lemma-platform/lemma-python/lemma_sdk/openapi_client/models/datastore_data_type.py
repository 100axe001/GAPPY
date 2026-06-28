from enum import Enum


class DatastoreDataType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    DATETIME = "DATETIME"
    ENUM = "ENUM"
    FILE_PATH = "FILE_PATH"
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    JSON = "JSON"
    SERIAL = "SERIAL"
    TEXT = "TEXT"
    USER = "USER"
    UUID = "UUID"
    VECTOR = "VECTOR"

    def __str__(self) -> str:
        return str(self.value)
