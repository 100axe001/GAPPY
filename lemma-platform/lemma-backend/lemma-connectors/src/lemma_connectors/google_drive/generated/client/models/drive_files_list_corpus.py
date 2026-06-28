from enum import Enum

class DriveFilesListCorpus(str, Enum):
    DOMAIN = "domain"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
