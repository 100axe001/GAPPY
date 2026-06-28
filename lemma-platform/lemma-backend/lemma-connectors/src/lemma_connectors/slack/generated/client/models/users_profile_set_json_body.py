from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UsersProfileSetJsonBody")



@_attrs_define
class UsersProfileSetJsonBody:
    """ 
        Attributes:
            name (str | Unset): Name of a single key to set. Usable only if `profile` is not passed.
            profile (str | Unset): Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may
                be set. Each field name is limited to 255 characters.
            user (str | Unset): ID of user to change. This argument may only be specified by team admins on paid teams.
            value (str | Unset): Value to set a single key to. Usable only if `profile` is not passed.
     """

    name: str | Unset = UNSET
    profile: str | Unset = UNSET
    user: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        profile = self.profile

        user = self.user

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if profile is not UNSET:
            field_dict["profile"] = profile
        if user is not UNSET:
            field_dict["user"] = user
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        profile = d.pop("profile", UNSET)

        user = d.pop("user", UNSET)

        value = d.pop("value", UNSET)

        users_profile_set_json_body = cls(
            name=name,
            profile=profile,
            user=user,
            value=value,
        )


        users_profile_set_json_body.additional_properties = d
        return users_profile_set_json_body

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
