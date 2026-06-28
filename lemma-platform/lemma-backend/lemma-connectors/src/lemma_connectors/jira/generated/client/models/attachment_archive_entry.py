from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttachmentArchiveEntry")



@_attrs_define
class AttachmentArchiveEntry:
    """ 
        Attributes:
            abbreviated_name (str | Unset):
            entry_index (int | Unset):
            media_type (str | Unset):
            name (str | Unset):
            size (int | Unset):
     """

    abbreviated_name: str | Unset = UNSET
    entry_index: int | Unset = UNSET
    media_type: str | Unset = UNSET
    name: str | Unset = UNSET
    size: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        abbreviated_name = self.abbreviated_name

        entry_index = self.entry_index

        media_type = self.media_type

        name = self.name

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if abbreviated_name is not UNSET:
            field_dict["abbreviatedName"] = abbreviated_name
        if entry_index is not UNSET:
            field_dict["entryIndex"] = entry_index
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        abbreviated_name = d.pop("abbreviatedName", UNSET)

        entry_index = d.pop("entryIndex", UNSET)

        media_type = d.pop("mediaType", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        attachment_archive_entry = cls(
            abbreviated_name=abbreviated_name,
            entry_index=entry_index,
            media_type=media_type,
            name=name,
            size=size,
        )

        return attachment_archive_entry

