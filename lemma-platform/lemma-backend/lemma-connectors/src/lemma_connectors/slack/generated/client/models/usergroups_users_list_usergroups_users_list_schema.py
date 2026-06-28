from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UsergroupsUsersListUsergroupsUsersListSchema")



@_attrs_define
class UsergroupsUsersListUsergroupsUsersListSchema:
    """ Schema for successful response from usergroups.users.list method

        Attributes:
            ok (bool):
            users (list[str]):
     """

    ok: bool
    users: list[str]





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        users = self.users




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "users": users,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        users = cast(list[str], d.pop("users"))


        usergroups_users_list_usergroups_users_list_schema = cls(
            ok=ok,
            users=users,
        )

        return usergroups_users_list_usergroups_users_list_schema

