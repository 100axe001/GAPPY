from __future__ import annotations

from ..openapi_client.api.agent_surfaces import (
    agent_surface_channels,
    agent_surface_delete,
    agent_surface_get,
    agent_surface_list,
    agent_surface_setup,
    agent_surface_upsert,
)
from ..openapi_client.models.agent_surface_list_response import AgentSurfaceListResponse
from ..openapi_client.models.agent_surface_response import AgentSurfaceResponse
from ..openapi_client.models.available_surface_channels_response import (
    AvailableSurfaceChannelsResponse,
)
from ..openapi_client.models.surface_setup_response import SurfaceSetupResponse
from ..openapi_client.models.surface_upsert_request import SurfaceUpsertRequest
from .base import BoundResource


class PodSurfaces(BoundResource):
    """Agent surfaces, addressed by platform (a surface is unique per pod+platform).

    One ``upsert`` write covers create, config/channel edits, account and
    credential changes, and enable/disable (via ``is_enabled``). ``delete``
    removes the surface entirely and frees its account for reuse. ``setup``
    merges live readiness, admin-consent, and the platform checklist.
    """

    def list(self, *, limit: int = 100) -> AgentSurfaceListResponse:
        return self._call(agent_surface_list, self._pod_uuid(), limit=limit)

    def upsert(
        self, platform: str, request: SurfaceUpsertRequest | dict
    ) -> AgentSurfaceResponse:
        return self._call(
            agent_surface_upsert,
            self._pod_uuid(),
            platform,
            body=request,
            body_model=SurfaceUpsertRequest,
        )

    def get(self, platform: str) -> AgentSurfaceResponse:
        return self._call(agent_surface_get, self._pod_uuid(), platform)

    def delete(self, platform: str) -> None:
        self._call(agent_surface_delete, self._pod_uuid(), platform)

    def setup(self, platform: str) -> SurfaceSetupResponse:
        return self._call(agent_surface_setup, self._pod_uuid(), platform)

    def channels(self, platform: str) -> AvailableSurfaceChannelsResponse:
        return self._call(agent_surface_channels, self._pod_uuid(), platform)
