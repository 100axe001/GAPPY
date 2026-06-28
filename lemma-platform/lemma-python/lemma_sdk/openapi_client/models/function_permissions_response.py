from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_resource_permission_response import (
        FunctionResourcePermissionResponse,
    )


T = TypeVar("T", bound="FunctionPermissionsResponse")


@_attrs_define
class FunctionPermissionsResponse:
    """
    Attributes:
        function_id (UUID):
        function_name (str):
        grants (list[FunctionResourcePermissionResponse] | Unset):
    """

    function_id: UUID
    function_name: str
    grants: list[FunctionResourcePermissionResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_id = str(self.function_id)

        function_name = self.function_name

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
                "function_id": function_id,
                "function_name": function_name,
            }
        )
        if grants is not UNSET:
            field_dict["grants"] = grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_resource_permission_response import (
            FunctionResourcePermissionResponse,
        )

        d = dict(src_dict)
        function_id = UUID(d.pop("function_id"))

        function_name = d.pop("function_name")

        _grants = d.pop("grants", UNSET)
        grants: list[FunctionResourcePermissionResponse] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = FunctionResourcePermissionResponse.from_dict(
                    grants_item_data
                )

                grants.append(grants_item)

        function_permissions_response = cls(
            function_id=function_id,
            function_name=function_name,
            grants=grants,
        )

        function_permissions_response.additional_properties = d
        return function_permissions_response

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
