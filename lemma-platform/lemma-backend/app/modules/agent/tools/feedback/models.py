from __future__ import annotations

from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class FeedbackCategory(str, Enum):
    SYSTEM_ISSUE = "SYSTEM_ISSUE"
    SKILL_ISSUE = "SKILL_ISSUE"
    INCORRECT_KNOWLEDGE = "INCORRECT_KNOWLEDGE"
    TOOLING_ISSUE = "TOOLING_ISSUE"
    OTHER = "OTHER"


class ReportFeedbackRequest(BaseModel):
    """Request payload for maintainer feedback reports."""

    category: FeedbackCategory = Field(
        description="High-level category for the feedback report."
    )
    subject: str = Field(
        min_length=3,
        max_length=255,
        description="Short subject line summarizing the report.",
    )
    issue_encountered: str = Field(
        min_length=3,
        description="What issue, problem, or incorrect information was encountered.",
    )
    expected_behavior: str = Field(
        min_length=3,
        description="What the caller expected to happen instead.",
    )
    actual_behavior: str = Field(
        min_length=3,
        description="What actually happened.",
    )
    suggested_next_steps: str | None = Field(
        default=None,
        description="Optional proposed fixes, follow-ups, or next steps.",
    )


class ReportFeedbackResponse(BaseModel):
    """Response payload for maintainer feedback reports."""

    success: bool = Field(description="Whether the feedback was recorded successfully.")
    feedback_id: UUID | None = Field(
        default=None,
        description="Identifier of the created feedback report.",
    )
    user_id: UUID | None = Field(
        default=None,
        description="Authenticated user associated with the report.",
    )
    agent_id: UUID | None = Field(
        default=None,
        description="Delegated agent associated with the report, if available.",
    )
    message: str | None = Field(
        default=None,
        description="Human-readable status message.",
    )
