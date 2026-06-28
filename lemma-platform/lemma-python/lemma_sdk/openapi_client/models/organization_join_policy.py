from enum import Enum


class OrganizationJoinPolicy(str, Enum):
    EMAIL_DOMAIN = "EMAIL_DOMAIN"
    INVITE_ONLY = "INVITE_ONLY"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
