from enum import Enum


class FeedbackCategory(str, Enum):
    INCORRECT_KNOWLEDGE = "INCORRECT_KNOWLEDGE"
    OTHER = "OTHER"
    SKILL_ISSUE = "SKILL_ISSUE"
    SYSTEM_ISSUE = "SYSTEM_ISSUE"
    TOOLING_ISSUE = "TOOLING_ISSUE"

    def __str__(self) -> str:
        return str(self.value)
