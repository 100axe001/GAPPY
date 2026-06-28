from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="MessageObjectAttachmentsItem")



@_attrs_define
class MessageObjectAttachmentsItem:
    """ 
        Attributes:
            id (int):
            fallback (str | Unset):
            image_bytes (int | Unset):
            image_height (int | Unset):
            image_url (str | Unset):
            image_width (int | Unset):
     """

    id: int
    fallback: str | Unset = UNSET
    image_bytes: int | Unset = UNSET
    image_height: int | Unset = UNSET
    image_url: str | Unset = UNSET
    image_width: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        fallback = self.fallback

        image_bytes = self.image_bytes

        image_height = self.image_height

        image_url = self.image_url

        image_width = self.image_width


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if fallback is not UNSET:
            field_dict["fallback"] = fallback
        if image_bytes is not UNSET:
            field_dict["image_bytes"] = image_bytes
        if image_height is not UNSET:
            field_dict["image_height"] = image_height
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if image_width is not UNSET:
            field_dict["image_width"] = image_width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        fallback = d.pop("fallback", UNSET)

        image_bytes = d.pop("image_bytes", UNSET)

        image_height = d.pop("image_height", UNSET)

        image_url = d.pop("image_url", UNSET)

        image_width = d.pop("image_width", UNSET)

        message_object_attachments_item = cls(
            id=id,
            fallback=fallback,
            image_bytes=image_bytes,
            image_height=image_height,
            image_url=image_url,
            image_width=image_width,
        )

        return message_object_attachments_item

