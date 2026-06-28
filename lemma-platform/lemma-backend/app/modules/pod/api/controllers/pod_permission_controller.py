"""Pod-owned permission catalog routes."""

from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from app.core.authorization.context import ResourceRef
from app.core.authorization.dependencies import PodContextDep, require_action
from app.core.authorization.permissions import PERMISSION_BY_ID
from app.core.authorization.permissions import PERMISSION_DEFINITIONS
from app.core.authorization.permissions import Permissions
from app.modules.pod.api.schemas.pod_schemas import (
    PodEffectivePermissionsResponse,
    PodPermissionCatalogResponse,
    PodPermissionResponse,
)

router = APIRouter(prefix="/pods/{pod_id}/permissions", tags=["Pod Permissions"])


@router.get(
    "/catalog",
    response_model=PodPermissionCatalogResponse,
    operation_id="pod.permissions.catalog",
    dependencies=[require_action(Permissions.POD_READ)],
)
async def get_pod_permission_catalog(pod_id: UUID) -> PodPermissionCatalogResponse:
    _ = pod_id
    return PodPermissionCatalogResponse(
        items=[
            PodPermissionResponse(
                id=item.id,
                scope=item.scope.value,
                resource_type=item.resource_type,
                description=item.description,
                system_only=item.system_only,
            )
            for item in PERMISSION_DEFINITIONS
            if item.scope.value == "POD"
        ]
    )


@router.get(
    "/me",
    response_model=PodEffectivePermissionsResponse,
    operation_id="pod.permissions.me",
)
async def get_my_pod_permissions(
    pod_id: UUID,
    ctx: PodContextDep,
) -> PodEffectivePermissionsResponse:
    resource = ResourceRef.pod(pod_id)
    actions = [
        permission_id
        for permission_id in sorted(PERMISSION_BY_ID)
        if await ctx.can(permission_id, resource)
    ]
    return PodEffectivePermissionsResponse(pod_id=pod_id, actions=actions)
