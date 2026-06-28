from enum import Enum


class SurfacePlatform(str, Enum):
    GMAIL = "GMAIL"
    OUTLOOK = "OUTLOOK"
    SLACK = "SLACK"
    TEAMS = "TEAMS"
    TELEGRAM = "TELEGRAM"
    WHATSAPP = "WHATSAPP"

    def __str__(self) -> str:
        return str(self.value)
