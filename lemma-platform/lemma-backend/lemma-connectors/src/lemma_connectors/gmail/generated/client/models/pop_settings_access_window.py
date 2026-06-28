from enum import Enum

class PopSettingsAccessWindow(str, Enum):
    ACCESSWINDOWUNSPECIFIED = "accessWindowUnspecified"
    ALLMAIL = "allMail"
    DISABLED = "disabled"
    FROMNOWON = "fromNowOn"

    def __str__(self) -> str:
        return str(self.value)
