from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PermissionTeamDrivePermissionDetailsItem")



@_attrs_define
class PermissionTeamDrivePermissionDetailsItem:
    """ 
        Attributes:
            inherited (bool | Unset): Deprecated - use permissionDetails/inherited instead.
            inherited_from (str | Unset): Deprecated - use permissionDetails/inheritedFrom instead.
            role (str | Unset): Deprecated - use permissionDetails/role instead.
            team_drive_permission_type (str | Unset): Deprecated - use permissionDetails/permissionType instead.
     """

    inherited: bool | Unset = UNSET
    inherited_from: str | Unset = UNSET
    role: str | Unset = UNSET
    team_drive_permission_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        inherited = self.inherited

        inherited_from = self.inherited_from

        role = self.role

        team_drive_permission_type = self.team_drive_permission_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inherited is not UNSET:
            field_dict["inherited"] = inherited
        if inherited_from is not UNSET:
            field_dict["inheritedFrom"] = inherited_from
        if role is not UNSET:
            field_dict["role"] = role
        if team_drive_permission_type is not UNSET:
            field_dict["teamDrivePermissionType"] = team_drive_permission_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inherited = d.pop("inherited", UNSET)

        inherited_from = d.pop("inheritedFrom", UNSET)

        role = d.pop("role", UNSET)

        team_drive_permission_type = d.pop("teamDrivePermissionType", UNSET)

        permission_team_drive_permission_details_item = cls(
            inherited=inherited,
            inherited_from=inherited_from,
            role=role,
            team_drive_permission_type=team_drive_permission_type,
        )


        permission_team_drive_permission_details_item.additional_properties = d
        return permission_team_drive_permission_details_item

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
