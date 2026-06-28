from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_role import OrganizationRole
from ..models.pod_role import PodRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="PodJoinRequestApproveRequest")


@_attrs_define
class PodJoinRequestApproveRequest:
    """
    Attributes:
        org_role (OrganizationRole | Unset): Roles for organization membership.
        pod_role (PodRole | Unset): Explicit pod role names used across authorization and pod APIs.
    """

    org_role: OrganizationRole | Unset = UNSET
    pod_role: PodRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_role: str | Unset = UNSET
        if not isinstance(self.org_role, Unset):
            org_role = self.org_role.value

        pod_role: str | Unset = UNSET
        if not isinstance(self.pod_role, Unset):
            pod_role = self.pod_role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_role is not UNSET:
            field_dict["org_role"] = org_role
        if pod_role is not UNSET:
            field_dict["pod_role"] = pod_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _org_role = d.pop("org_role", UNSET)
        org_role: OrganizationRole | Unset
        if isinstance(_org_role, Unset):
            org_role = UNSET
        else:
            org_role = OrganizationRole(_org_role)

        _pod_role = d.pop("pod_role", UNSET)
        pod_role: PodRole | Unset
        if isinstance(_pod_role, Unset):
            pod_role = UNSET
        else:
            pod_role = PodRole(_pod_role)

        pod_join_request_approve_request = cls(
            org_role=org_role,
            pod_role=pod_role,
        )

        pod_join_request_approve_request.additional_properties = d
        return pod_join_request_approve_request

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
