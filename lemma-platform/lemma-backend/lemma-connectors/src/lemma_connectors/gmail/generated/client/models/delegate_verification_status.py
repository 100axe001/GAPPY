from enum import Enum

class DelegateVerificationStatus(str, Enum):
    ACCEPTED = "accepted"
    EXPIRED = "expired"
    PENDING = "pending"
    REJECTED = "rejected"
    VERIFICATIONSTATUSUNSPECIFIED = "verificationStatusUnspecified"

    def __str__(self) -> str:
        return str(self.value)
