from enum import Enum

class SmtpMsaSecurityMode(str, Enum):
    NONE = "none"
    SECURITYMODEUNSPECIFIED = "securityModeUnspecified"
    SSL = "ssl"
    STARTTLS = "starttls"

    def __str__(self) -> str:
        return str(self.value)
