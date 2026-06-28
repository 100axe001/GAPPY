from enum import Enum


class PodJoinPolicy(str, Enum):
    INVITE_ONLY = "INVITE_ONLY"
    ORG_MEMBERS = "ORG_MEMBERS"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
