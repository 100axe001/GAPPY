from enum import Enum

class GetTrashedFieldsPaginatedExpand(str, Enum):
    NAME = "name"
    PLANNEDDELETIONDATE = "plannedDeletionDate"
    PROJECTSCOUNT = "projectsCount"
    TRASHDATE = "trashDate"
    VALUE_1 = "-name"
    VALUE_10 = "-projectsCount"
    VALUE_11 = "+projectsCount"
    VALUE_2 = "+name"
    VALUE_4 = "-trashDate"
    VALUE_5 = "+trashDate"
    VALUE_7 = "-plannedDeletionDate"
    VALUE_8 = "+plannedDeletionDate"

    def __str__(self) -> str:
        return str(self.value)
