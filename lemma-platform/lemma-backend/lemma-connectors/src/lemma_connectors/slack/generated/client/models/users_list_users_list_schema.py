from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UsersListUsersListSchema")



@_attrs_define
class UsersListUsersListSchema:
    """ Schema for successful response from users.list method

        Attributes:
            cache_ts (int):
            members (list[Any]):
            ok (bool):
            response_metadata (Any | Unset):
     """

    cache_ts: int
    members: list[Any]
    ok: bool
    response_metadata: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cache_ts = self.cache_ts

        members = self.members



        ok = self.ok

        response_metadata = self.response_metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cache_ts": cache_ts,
            "members": members,
            "ok": ok,
        })
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_ts = d.pop("cache_ts")

        members = cast(list[Any], d.pop("members"))


        ok = d.pop("ok")

        response_metadata = d.pop("response_metadata", UNSET)

        users_list_users_list_schema = cls(
            cache_ts=cache_ts,
            members=members,
            ok=ok,
            response_metadata=response_metadata,
        )

        return users_list_users_list_schema

