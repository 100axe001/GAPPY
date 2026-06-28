from enum import Enum

class EventNotificationNotificationType(str, Enum):
    ALLWATCHERS = "AllWatchers"
    COMPONENTLEAD = "ComponentLead"
    CURRENTASSIGNEE = "CurrentAssignee"
    CURRENTUSER = "CurrentUser"
    EMAILADDRESS = "EmailAddress"
    GROUP = "Group"
    GROUPCUSTOMFIELD = "GroupCustomField"
    PROJECTLEAD = "ProjectLead"
    PROJECTROLE = "ProjectRole"
    REPORTER = "Reporter"
    USER = "User"
    USERCUSTOMFIELD = "UserCustomField"

    def __str__(self) -> str:
        return str(self.value)
