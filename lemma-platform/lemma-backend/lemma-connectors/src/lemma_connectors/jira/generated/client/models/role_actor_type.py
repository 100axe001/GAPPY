from enum import Enum

class RoleActorType(str, Enum):
    ATLASSIAN_GROUP_ROLE_ACTOR = "atlassian-group-role-actor"
    ATLASSIAN_USER_ROLE_ACTOR = "atlassian-user-role-actor"

    def __str__(self) -> str:
        return str(self.value)
