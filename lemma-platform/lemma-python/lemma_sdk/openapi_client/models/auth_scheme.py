from enum import Enum


class AuthScheme(str, Enum):
    API_KEY = "API_KEY"
    NOAUTH = "NOAUTH"
    OAUTH2 = "OAUTH2"

    def __str__(self) -> str:
        return str(self.value)
