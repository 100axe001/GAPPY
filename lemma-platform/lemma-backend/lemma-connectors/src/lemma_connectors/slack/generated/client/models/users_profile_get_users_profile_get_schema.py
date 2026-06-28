from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_profile_object import UserProfileObject





T = TypeVar("T", bound="UsersProfileGetUsersProfileGetSchema")



@_attrs_define
class UsersProfileGetUsersProfileGetSchema:
    """ Schema for successful response from users.profile.get method

        Attributes:
            ok (bool):
            profile (UserProfileObject):
     """

    ok: bool
    profile: UserProfileObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_object import UserProfileObject
        ok = self.ok

        profile = self.profile.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "profile": profile,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile_object import UserProfileObject
        d = dict(src_dict)
        ok = d.pop("ok")

        profile = UserProfileObject.from_dict(d.pop("profile"))




        users_profile_get_users_profile_get_schema = cls(
            ok=ok,
            profile=profile,
        )

        return users_profile_get_users_profile_get_schema

