from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="BotProfileObjectIcons")



@_attrs_define
class BotProfileObjectIcons:
    """ 
        Attributes:
            image_36 (str):
            image_48 (str):
            image_72 (str):
     """

    image_36: str
    image_48: str
    image_72: str





    def to_dict(self) -> dict[str, Any]:
        image_36 = self.image_36

        image_48 = self.image_48

        image_72 = self.image_72


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "image_36": image_36,
            "image_48": image_48,
            "image_72": image_72,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_36 = d.pop("image_36")

        image_48 = d.pop("image_48")

        image_72 = d.pop("image_72")

        bot_profile_object_icons = cls(
            image_36=image_36,
            image_48=image_48,
            image_72=image_72,
        )

        return bot_profile_object_icons

