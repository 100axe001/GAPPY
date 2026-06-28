from __future__ import annotations

from ..openapi_client.api.pod_members import pod_member_list
from ..openapi_client.models.pod_member_list_response import PodMemberListResponse
from ..openapi_client.types import UNSET
from .base import BoundResource


class PodMembers(BoundResource):
    def list(
        self,
        *,
        limit: int = 100,
        page_token: str | None = None,
    ) -> PodMemberListResponse:
        return self._call(
            pod_member_list,
            self._pod_uuid(),
            limit=limit,
            page_token=page_token if page_token is not None else UNSET,
        )
