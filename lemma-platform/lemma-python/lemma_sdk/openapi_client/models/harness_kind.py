from enum import Enum


class HarnessKind(str, Enum):
    CLAUDE_CODE = "CLAUDE_CODE"
    CODEX = "CODEX"
    LEMMA = "LEMMA"
    OPENCODE = "OPENCODE"

    def __str__(self) -> str:
        return str(self.value)
