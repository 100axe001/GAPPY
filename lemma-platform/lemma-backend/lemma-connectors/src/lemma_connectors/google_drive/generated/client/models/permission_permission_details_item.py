from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PermissionPermissionDetailsItem")



@_attrs_define
class PermissionPermissionDetailsItem:
    """ 
        Attributes:
            inherited (bool | Unset): Whether this permission is inherited. This field is always populated. This is an
                output-only field.
            inherited_from (str | Unset): The ID of the item from which this permission is inherited. This is an output-only
                field.
            permission_type (str | Unset): The permission type for this user. While new values may be added in future, the
                following are currently allowed:
                - file
                - member
            role (str | Unset): The primary role for this user. While new values may be added in the future, the following
                are currently allowed:
                - organizer
                - fileOrganizer
                - writer
                - commenter
                - reader
     """

    inherited: bool | Unset = UNSET
    inherited_from: str | Unset = UNSET
    permission_type: str | Unset = UNSET
    role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        inherited = self.inherited

        inherited_from = self.inherited_from

        permission_type = self.permission_type

        role = self.role


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inherited is not UNSET:
            field_dict["inherited"] = inherited
        if inherited_from is not UNSET:
            field_dict["inheritedFrom"] = inherited_from
        if permission_type is not UNSET:
            field_dict["permissionType"] = permission_type
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inherited = d.pop("inherited", UNSET)

        inherited_from = d.pop("inheritedFrom", UNSET)

        permission_type = d.pop("permissionType", UNSET)

        role = d.pop("role", UNSET)

        permission_permission_details_item = cls(
            inherited=inherited,
            inherited_from=inherited_from,
            permission_type=permission_type,
            role=role,
        )


        permission_permission_details_item.additional_properties = d
        return permission_permission_details_item

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
