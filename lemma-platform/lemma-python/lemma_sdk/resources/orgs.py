from __future__ import annotations

from ..openapi_client.api.organizations import (
    org_create,
    org_get,
    org_list,
    org_member_list,
)
from ..openapi_client.models.organization_create_request import OrganizationCreateRequest
from ..openapi_client.models.organization_list_response import OrganizationListResponse
from ..openapi_client.models.organization_member_list_response import (
    OrganizationMemberListResponse,
)
from ..openapi_client.models.organization_response import OrganizationResponse
from .base import BoundResource, Resource, as_uuid


class Orgs(Resource):
    def list(self, *, limit: int = 100) -> OrganizationListResponse:
        return self._call(org_list, limit=limit)

    def create(self, *, name: str) -> OrganizationResponse:
        return self._call(
            org_create,
            body={"name": name},
            body_model=OrganizationCreateRequest,
        )

    def get(self, org_id: str) -> OrganizationResponse:
        return self._call(org_get, as_uuid(org_id))


class BoundOrg(BoundResource):
    def get(self) -> OrganizationResponse:
        return self._call(org_get, self._org_uuid())

    def members(self, *, limit: int = 100) -> OrganizationMemberListResponse:
        return self._call(org_member_list, self._org_uuid(), limit=limit)
