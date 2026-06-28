from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UsersLookupByEmailUsersLookupByEmailSuccessSchema")



@_attrs_define
class UsersLookupByEmailUsersLookupByEmailSuccessSchema:
    """ Schema for successful response from users.lookupByEmail method

        Attributes:
            ok (bool):
            user (Any):
     """

    ok: bool
    user: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        user = self.user


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "ok": ok,
            "user": user,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        user = d.pop("user")

        users_lookup_by_email_users_lookup_by_email_success_schema = cls(
            ok=ok,
            user=user,
        )


        users_lookup_by_email_users_lookup_by_email_success_schema.additional_properties = d
        return users_lookup_by_email_users_lookup_by_email_success_schema

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
