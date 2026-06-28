from enum import Enum


class CredentialTypes(str, Enum):
    API_KEY = "api_key"
    OAUTH2 = "oauth2"

    def __str__(self) -> str:
        return str(self.value)
