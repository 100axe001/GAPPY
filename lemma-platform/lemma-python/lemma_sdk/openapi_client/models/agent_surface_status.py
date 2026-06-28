from enum import Enum


class AgentSurfaceStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    INACTIVE = "INACTIVE"
    NEEDS_SETUP = "NEEDS_SETUP"
    PENDING_ADMIN_CONSENT = "PENDING_ADMIN_CONSENT"

    def __str__(self) -> str:
        return str(self.value)
