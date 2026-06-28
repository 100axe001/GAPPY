from enum import Enum

class MigrationResourceUpdateEntityPropertiesValuePutEntityType(str, Enum):
    BOARDPROPERTY = "BoardProperty"
    COMMENTPROPERTY = "CommentProperty"
    DASHBOARDITEMPROPERTY = "DashboardItemProperty"
    ISSUEPROPERTY = "IssueProperty"
    ISSUETYPEPROPERTY = "IssueTypeProperty"
    PROJECTPROPERTY = "ProjectProperty"
    SPRINTPROPERTY = "SprintProperty"
    USERPROPERTY = "UserProperty"
    WORKLOGPROPERTY = "WorklogProperty"

    def __str__(self) -> str:
        return str(self.value)
