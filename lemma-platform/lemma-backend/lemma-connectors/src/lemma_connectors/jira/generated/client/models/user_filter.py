from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UserFilter")



@_attrs_define
class UserFilter:
    """ Filter for a User Picker (single) custom field.

        Attributes:
            enabled (bool): Whether the filter is enabled.
            groups (list[str] | Unset): User groups autocomplete suggestion users must belong to. If not provided, the
                default values are used. A maximum of 10 groups can be provided.
            role_ids (list[int] | Unset): Roles that autocomplete suggestion users must belong to. If not provided, the
                default values are used. A maximum of 10 roles can be provided.
     """

    enabled: bool
    groups: list[str] | Unset = UNSET
    role_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups



        role_ids: list[int] | Unset = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enabled": enabled,
        })
        if groups is not UNSET:
            field_dict["groups"] = groups
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        groups = cast(list[str], d.pop("groups", UNSET))


        role_ids = cast(list[int], d.pop("roleIds", UNSET))


        user_filter = cls(
            enabled=enabled,
            groups=groups,
            role_ids=role_ids,
        )


        user_filter.additional_properties = d
        return user_filter

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
