"""Default model selection for agent runs, and the port a billing/plan provider
implements to make it plan-aware.

The value object lives in the agent domain (its consumer) so agent never imports
billing; billing implements ``SubscriptionModelsPort`` and registers it. Without
a provider, agent uses these built-in defaults.
"""

from __future__ import annotations

from typing import Protocol
from uuid import UUID

from pydantic import BaseModel


class SubscriptionModels(BaseModel):
    """The models an agent run should use, by purpose."""

    conversation_model: str = "kimi-k2.6"
    agent_model: str = "kimi-k2.6"
    summarization_model: str = "kimi-k2.6"
    file_generation_model: str = "kimi-k2.6"


class SubscriptionModelsPort(Protocol):
    """Resolves the models available to a user (plan-aware in the billing impl)."""

    async def get_models_for_user(self, user_id: UUID) -> SubscriptionModels: ...
