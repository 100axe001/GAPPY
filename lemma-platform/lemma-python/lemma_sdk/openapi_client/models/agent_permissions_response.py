from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_resource_permission_response import (
        AgentResourcePermissionResponse,
    )


T = TypeVar("T", bound="AgentPermissionsResponse")


@_attrs_define
class AgentPermissionsResponse:
    """
    Attributes:
        agent_id (UUID):
        agent_name (str):
        grants (list[AgentResourcePermissionResponse] | Unset):
    """

    agent_id: UUID
    agent_name: str
    grants: list[AgentResourcePermissionResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        agent_name = self.agent_name

        grants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grants, Unset):
            grants = []
            for grants_item_data in self.grants:
                grants_item = grants_item_data.to_dict()
                grants.append(grants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
            }
        )
        if grants is not UNSET:
            field_dict["grants"] = grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_resource_permission_response import (
            AgentResourcePermissionResponse,
        )

        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        agent_name = d.pop("agent_name")

        _grants = d.pop("grants", UNSET)
        grants: list[AgentResourcePermissionResponse] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = AgentResourcePermissionResponse.from_dict(
                    grants_item_data
                )

                grants.append(grants_item)

        agent_permissions_response = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            grants=grants,
        )

        agent_permissions_response.additional_properties = d
        return agent_permissions_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
