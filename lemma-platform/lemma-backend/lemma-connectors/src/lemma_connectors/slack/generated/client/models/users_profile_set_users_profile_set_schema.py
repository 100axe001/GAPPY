from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_profile_object import UserProfileObject





T = TypeVar("T", bound="UsersProfileSetUsersProfileSetSchema")



@_attrs_define
class UsersProfileSetUsersProfileSetSchema:
    """ Schema for successful response from users.profile.set method

        Attributes:
            ok (bool):
            profile (UserProfileObject):
            username (str):
            email_pending (str | Unset):
     """

    ok: bool
    profile: UserProfileObject
    username: str
    email_pending: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_object import UserProfileObject
        ok = self.ok

        profile = self.profile.to_dict()

        username = self.username

        email_pending = self.email_pending


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "profile": profile,
            "username": username,
        })
        if email_pending is not UNSET:
            field_dict["email_pending"] = email_pending

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile_object import UserProfileObject
        d = dict(src_dict)
        ok = d.pop("ok")

        profile = UserProfileObject.from_dict(d.pop("profile"))




        username = d.pop("username")

        email_pending = d.pop("email_pending", UNSET)

        users_profile_set_users_profile_set_schema = cls(
            ok=ok,
            profile=profile,
            username=username,
            email_pending=email_pending,
        )

        return users_profile_set_users_profile_set_schema

