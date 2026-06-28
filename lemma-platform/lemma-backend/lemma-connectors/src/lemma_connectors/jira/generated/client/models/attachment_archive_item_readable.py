from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AttachmentArchiveItemReadable")



@_attrs_define
class AttachmentArchiveItemReadable:
    """ Metadata for an item in an attachment archive.

        Attributes:
            index (int | Unset): The position of the item within the archive.
            label (str | Unset): The label for the archive item.
            media_type (str | Unset): The MIME type of the archive item.
            path (str | Unset): The path of the archive item.
            size (str | Unset): The size of the archive item.
     """

    index: int | Unset = UNSET
    label: str | Unset = UNSET
    media_type: str | Unset = UNSET
    path: str | Unset = UNSET
    size: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        index = self.index

        label = self.label

        media_type = self.media_type

        path = self.path

        size = self.size


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if label is not UNSET:
            field_dict["label"] = label
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        label = d.pop("label", UNSET)

        media_type = d.pop("mediaType", UNSET)

        path = d.pop("path", UNSET)

        size = d.pop("size", UNSET)

        attachment_archive_item_readable = cls(
            index=index,
            label=label,
            media_type=media_type,
            path=path,
            size=size,
        )

        return attachment_archive_item_readable

