from enum import Enum


class AgentRunApprovalDecision(str, Enum):
    APPROVE_FOR_SESSION = "APPROVE_FOR_SESSION"
    APPROVE_ONCE = "APPROVE_ONCE"
    DENY = "DENY"

    def __str__(self) -> str:
        return str(self.value)
