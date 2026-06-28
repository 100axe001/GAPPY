from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type import ResourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_access_grant_response import ResourceAccessGrantResponse


T = TypeVar("T", bound="ResourceAccessResponse")


@_attrs_define
class ResourceAccessResponse:
    """
    Attributes:
        resource_name (str):
        resource_type (ResourceType):
        grants (list[ResourceAccessGrantResponse] | Unset):
    """

    resource_name: str
    resource_type: ResourceType
    grants: list[ResourceAccessGrantResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_name = self.resource_name

        resource_type = self.resource_type.value

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
                "resource_name": resource_name,
                "resource_type": resource_type,
            }
        )
        if grants is not UNSET:
            field_dict["grants"] = grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_access_grant_response import ResourceAccessGrantResponse

        d = dict(src_dict)
        resource_name = d.pop("resource_name")

        resource_type = ResourceType(d.pop("resource_type"))

        _grants = d.pop("grants", UNSET)
        grants: list[ResourceAccessGrantResponse] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = ResourceAccessGrantResponse.from_dict(grants_item_data)

                grants.append(grants_item)

        resource_access_response = cls(
            resource_name=resource_name,
            resource_type=resource_type,
            grants=grants,
        )

        resource_access_response.additional_properties = d
        return resource_access_response

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
