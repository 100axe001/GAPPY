from enum import Enum

class ChartAxisViewWindowOptionsViewWindowMode(str, Enum):
    DEFAULT_VIEW_WINDOW_MODE = "DEFAULT_VIEW_WINDOW_MODE"
    EXPLICIT = "EXPLICIT"
    PRETTY = "PRETTY"
    VIEW_WINDOW_MODE_UNSUPPORTED = "VIEW_WINDOW_MODE_UNSUPPORTED"

    def __str__(self) -> str:
        return str(self.value)
