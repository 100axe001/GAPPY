from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.users_set_photo_users_set_photo_schema_profile import UsersSetPhotoUsersSetPhotoSchemaProfile





T = TypeVar("T", bound="UsersSetPhotoUsersSetPhotoSchema")



@_attrs_define
class UsersSetPhotoUsersSetPhotoSchema:
    """ Schema for successful response from users.setPhoto method

        Attributes:
            ok (bool):
            profile (UsersSetPhotoUsersSetPhotoSchemaProfile):
     """

    ok: bool
    profile: UsersSetPhotoUsersSetPhotoSchemaProfile





    def to_dict(self) -> dict[str, Any]:
        from ..models.users_set_photo_users_set_photo_schema_profile import UsersSetPhotoUsersSetPhotoSchemaProfile
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
        from ..models.users_set_photo_users_set_photo_schema_profile import UsersSetPhotoUsersSetPhotoSchemaProfile
        d = dict(src_dict)
        ok = d.pop("ok")

        profile = UsersSetPhotoUsersSetPhotoSchemaProfile.from_dict(d.pop("profile"))




        users_set_photo_users_set_photo_schema = cls(
            ok=ok,
            profile=profile,
        )

        return users_set_photo_users_set_photo_schema

