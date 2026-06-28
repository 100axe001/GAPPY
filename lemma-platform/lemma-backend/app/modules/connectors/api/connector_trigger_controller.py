from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Query

from app.core.api.dependencies import CurrentUser
from app.modules.connectors.api.dependencies import ConnectorTriggerServiceDep
from app.modules.connectors.api.schemas import (
    AppTriggerListResponseSchema,
    AppTriggerResponseSchema,
    AppTriggerSummaryResponseSchema,
)

router = APIRouter(
    prefix="/organizations/{organization_id}/connectors/{auth_config_name}/triggers",
    tags=["Connectors"],
)


@router.get(
    "",
    response_model=AppTriggerListResponseSchema,
    operation_id="connector.trigger.list",
    summary="List Connector Triggers",
)
async def list_triggers(
    organization_id: UUID,
    auth_config_name: str,
    user: CurrentUser,
    service: ConnectorTriggerServiceDep,
    search: str | None = Query(default=None),
    limit: int = Query(default=100, ge=1, le=1000),
) -> AppTriggerListResponseSchema:
    triggers = await service.list_triggers_for_auth_config(
        user_id=user.id,
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        search_query=search,
        limit=limit,
    )
    return AppTriggerListResponseSchema(
        items=[
            AppTriggerSummaryResponseSchema.model_validate(trigger)
            for trigger in triggers
        ],
        limit=limit,
        next_page_token=None,
    )


@router.get(
    "/{trigger_name}",
    response_model=AppTriggerResponseSchema,
    operation_id="connector.trigger.get",
    summary="Get Connector Trigger",
)
async def get_trigger(
    organization_id: UUID,
    auth_config_name: str,
    trigger_name: str,
    user: CurrentUser,
    service: ConnectorTriggerServiceDep,
) -> AppTriggerResponseSchema:
    trigger = await service.get_trigger_for_auth_config(
        user_id=user.id,
        organization_id=organization_id,
        auth_config_name=auth_config_name,
        trigger_name=trigger_name,
    )
    return AppTriggerResponseSchema.model_validate(trigger)
