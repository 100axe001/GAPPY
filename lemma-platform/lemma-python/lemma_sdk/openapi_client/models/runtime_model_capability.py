from enum import Enum


class RuntimeModelCapability(str, Enum):
    AUDIO = "AUDIO"
    REASONING = "REASONING"
    STRUCTURED_OUTPUT = "STRUCTURED_OUTPUT"
    TEXT = "TEXT"
    TOOLS = "TOOLS"
    VISION = "VISION"

    def __str__(self) -> str:
        return str(self.value)
