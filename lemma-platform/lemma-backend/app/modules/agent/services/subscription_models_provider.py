"""Extension point for a plan-aware :class:`SubscriptionModelsPort`.

Mirrors usage's limit provider: billing registers an implementation; with none
registered (e.g. no billing module), agent uses the built-in default models.
"""

from __future__ import annotations

from typing import Optional
from uuid import UUID

from app.modules.agent.domain.subscription_models import (
    SubscriptionModels,
    SubscriptionModelsPort,
)

_provider: Optional[SubscriptionModelsPort] = None


def configure_subscription_models_provider(
    provider: Optional[SubscriptionModelsPort],
) -> None:
    """Register (or clear) the subscription-models provider. Last write wins."""
    global _provider
    _provider = provider


async def resolve_subscription_models(user_id: UUID) -> SubscriptionModels:
    if _provider is None:
        return SubscriptionModels()
    return await _provider.get_models_for_user(user_id)
