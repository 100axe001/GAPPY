from enum import Enum


class OrganizationRole(str, Enum):
    ORG_EDITOR = "ORG_EDITOR"
    ORG_MEMBER = "ORG_MEMBER"
    ORG_OWNER = "ORG_OWNER"

    def __str__(self) -> str:
        return str(self.value)
