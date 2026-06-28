from enum import Enum

class SearchProjectsOrderBy(str, Enum):
    ARCHIVEDDATE = "archivedDate"
    CATEGORY = "category"
    DELETEDDATE = "deletedDate"
    ISSUECOUNT = "issueCount"
    KEY = "key"
    LASTISSUEUPDATEDDATE = "lastIssueUpdatedDate"
    NAME = "name"
    OWNER = "owner"
    VALUE_1 = "-category"
    VALUE_10 = "-owner"
    VALUE_11 = "+owner"
    VALUE_13 = "-issueCount"
    VALUE_14 = "+issueCount"
    VALUE_16 = "-lastIssueUpdatedDate"
    VALUE_17 = "+lastIssueUpdatedDate"
    VALUE_19 = "+archivedDate"
    VALUE_2 = "+category"
    VALUE_20 = "-archivedDate"
    VALUE_22 = "+deletedDate"
    VALUE_23 = "-deletedDate"
    VALUE_4 = "-key"
    VALUE_5 = "+key"
    VALUE_7 = "-name"
    VALUE_8 = "+name"

    def __str__(self) -> str:
        return str(self.value)
