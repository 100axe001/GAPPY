from enum import Enum

class ForwardingAddressVerificationStatus(str, Enum):
    ACCEPTED = "accepted"
    PENDING = "pending"
    VERIFICATIONSTATUSUNSPECIFIED = "verificationStatusUnspecified"

    def __str__(self) -> str:
        return str(self.value)
