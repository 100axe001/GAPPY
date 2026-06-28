from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UsersSetPhotoUsersSetPhotoSchemaProfile")



@_attrs_define
class UsersSetPhotoUsersSetPhotoSchemaProfile:
    """ 
        Attributes:
            avatar_hash (str):
            image_1024 (str):
            image_192 (str):
            image_24 (str):
            image_32 (str):
            image_48 (str):
            image_512 (str):
            image_72 (str):
            image_original (str):
     """

    avatar_hash: str
    image_1024: str
    image_192: str
    image_24: str
    image_32: str
    image_48: str
    image_512: str
    image_72: str
    image_original: str





    def to_dict(self) -> dict[str, Any]:
        avatar_hash = self.avatar_hash

        image_1024 = self.image_1024

        image_192 = self.image_192

        image_24 = self.image_24

        image_32 = self.image_32

        image_48 = self.image_48

        image_512 = self.image_512

        image_72 = self.image_72

        image_original = self.image_original


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "avatar_hash": avatar_hash,
            "image_1024": image_1024,
            "image_192": image_192,
            "image_24": image_24,
            "image_32": image_32,
            "image_48": image_48,
            "image_512": image_512,
            "image_72": image_72,
            "image_original": image_original,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_hash = d.pop("avatar_hash")

        image_1024 = d.pop("image_1024")

        image_192 = d.pop("image_192")

        image_24 = d.pop("image_24")

        image_32 = d.pop("image_32")

        image_48 = d.pop("image_48")

        image_512 = d.pop("image_512")

        image_72 = d.pop("image_72")

        image_original = d.pop("image_original")

        users_set_photo_users_set_photo_schema_profile = cls(
            avatar_hash=avatar_hash,
            image_1024=image_1024,
            image_192=image_192,
            image_24=image_24,
            image_32=image_32,
            image_48=image_48,
            image_512=image_512,
            image_72=image_72,
            image_original=image_original,
        )

        return users_set_photo_users_set_photo_schema_profile

