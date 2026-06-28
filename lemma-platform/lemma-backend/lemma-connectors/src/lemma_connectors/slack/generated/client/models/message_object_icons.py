from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MessageObjectIcons")



@_attrs_define
class MessageObjectIcons:
    """ 
        Attributes:
            emoji (str | Unset):
            image_64 (str | Unset):
     """

    emoji: str | Unset = UNSET
    image_64: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        emoji = self.emoji

        image_64 = self.image_64


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if emoji is not UNSET:
            field_dict["emoji"] = emoji
        if image_64 is not UNSET:
            field_dict["image_64"] = image_64

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emoji = d.pop("emoji", UNSET)

        image_64 = d.pop("image_64", UNSET)

        message_object_icons = cls(
            emoji=emoji,
            image_64=image_64,
        )

        return message_object_icons

