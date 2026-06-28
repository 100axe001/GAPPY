from enum import Enum

class DashboardGadgetColor(str, Enum):
    BLUE = "blue"
    CYAN = "cyan"
    GRAY = "gray"
    GREEN = "green"
    PURPLE = "purple"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"

    def __str__(self) -> str:
        return str(self.value)
