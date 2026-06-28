from enum import Enum


class AuthProvider(str, Enum):
    COMPOSIO = "COMPOSIO"
    LEMMA = "LEMMA"

    def __str__(self) -> str:
        return str(self.value)
