from __future__ import annotations

import asyncio
import os
from typing import Any, Callable

from app.modules.connectors.config import connector_settings
from app.modules.connectors.domain.errors import (
    ConnectorValidationError,
    OperationExecutionAccessDeniedError,
    OperationExecutionInfrastructureError,
    OperationExecutionNotFoundError,
    OperationExecutionUnauthorizedError,
    OperationExecutionValidationError,
)
from app.modules.connectors.domain.ports import (
    AppOperationGatewayPort,
    OperationDetailsPort,
)


ComposioClientFactory = Callable[[], Any]


class _UnsupportedComposioDetails(OperationDetailsPort):
    description: str | None = None
    input_schema_content: str | None = None
    output_schema_content: str | None = None


class ComposioOperationGateway(AppOperationGatewayPort):
    def __init__(
        self,
        composio_client_factory: ComposioClientFactory | None = None,
    ):
        self._composio_client_factory = composio_client_factory or self._default_client_factory

    def _default_client_factory(self) -> Any:
        from composio import Composio

        os.environ.setdefault("COMPOSIO_CACHE_DIR", "/tmp/composio")
        return Composio(api_key=connector_settings.composio_api_key)

    async def list_operations(self, connector_id: str) -> list[str]:
        raise ConnectorValidationError(
            "Operation discovery is served from the connector catalog."
        )

    async def get_operation_details(
        self, connector_id: str, operation_name: str
    ) -> OperationDetailsPort:
        return _UnsupportedComposioDetails()

    async def execute_operation(
        self,
        connector_id: str,
        operation_name: str,
        payload: dict[str, Any],
        third_party_credentials: dict[str, Any] | None,
        auth_token: str | None = None,
        api_url: str | None = None,
        provider: str | None = None,
    ) -> Any:
        del connector_id, auth_token, api_url, provider
        connection_id = (
            third_party_credentials.get("connection_id")
            if isinstance(third_party_credentials, dict)
            else None
        )
        if not connection_id:
            raise OperationExecutionValidationError(
                "Composio execution requires a connected account id.",
                details={"provider": "composio"},
            )

        def _execute() -> Any:
            composio = self._composio_client_factory()
            response = composio.tools.execute(
                operation_name,
                payload or {},
                connected_account_id=connection_id,
                dangerously_skip_version_check=True
            )
            if hasattr(response, "model_dump"):
                return response.model_dump()
            return response

        try:
            response = await asyncio.to_thread(_execute)
        except Exception as exc:
            raise OperationExecutionInfrastructureError(
                f"Composio tool execution failed for '{operation_name}': {exc}",
                details={
                    "provider": "composio",
                    "upstream_message": str(exc),
                },
            ) from exc
        if not isinstance(response, dict):
            return response

        if not response.get("successful", False):
            error = response.get("error") or "Unknown Composio execution error"
            details = {
                "provider": "composio",
                "error": error,
                "response": response,
            }
            normalized_error = str(error).lower()
            if normalized_error in {"not_found", "tool_not_found"}:
                raise OperationExecutionNotFoundError(
                    f"Composio tool execution failed for '{operation_name}': {error}",
                    details=details,
                )
            if normalized_error in {"unauthorized", "not_authed", "invalid_auth"}:
                raise OperationExecutionUnauthorizedError(
                    f"Composio tool execution failed for '{operation_name}': {error}",
                    details=details,
                )
            if normalized_error in {"forbidden", "missing_scope"}:
                raise OperationExecutionAccessDeniedError(
                    f"Composio tool execution failed for '{operation_name}': {error}",
                    details=details,
                )
            if normalized_error in {"invalid_arguments", "validation_error", "bad_request"}:
                raise OperationExecutionValidationError(
                    f"Composio tool execution failed for '{operation_name}': {error}",
                    details=details,
                )
            raise OperationExecutionInfrastructureError(
                f"Composio tool execution failed for '{operation_name}': {error}",
                details=details,
            )
        return response.get("data")
