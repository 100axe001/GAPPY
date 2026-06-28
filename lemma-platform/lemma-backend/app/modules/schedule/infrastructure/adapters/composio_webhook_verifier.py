from __future__ import annotations

from typing import Any, Dict

from app.modules.connectors.config import connector_settings
from app.modules.schedule.domain.interfaces import WebhookVerifier


class ComposioWebhookVerifier(WebhookVerifier):
    """Verify Composio webhooks through the official SDK."""

    def verify(self, payload: str, headers: Dict[str, Any]) -> Dict[str, Any]:
        from composio import Composio
        if not connector_settings.composio_webhook_secret:
            raise ValueError("Missing Composio webhook secret. Failed to verify")
        composio = Composio(api_key=connector_settings.composio_api_key or "webhook-verification")
        return composio.triggers.verify_webhook(
            id=headers.get("webhook-id", ""),
            payload=payload,
            signature=headers.get("webhook-signature", ""),
            timestamp=headers.get("webhook-timestamp", ""),
            secret=connector_settings.composio_webhook_secret or "",
        )
