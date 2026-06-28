from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.attachment_archive_item_readable import AttachmentArchiveItemReadable





T = TypeVar("T", bound="AttachmentArchiveMetadataReadable")



@_attrs_define
class AttachmentArchiveMetadataReadable:
    """ Metadata for an archive (for example a zip) and its contents.

        Attributes:
            entries (list[AttachmentArchiveItemReadable] | Unset): The list of the items included in the archive.
            id (int | Unset): The ID of the attachment.
            media_type (str | Unset): The MIME type of the attachment.
            name (str | Unset): The name of the archive file.
            total_entry_count (int | Unset): The number of items included in the archive.
     """

    entries: list[AttachmentArchiveItemReadable] | Unset = UNSET
    id: int | Unset = UNSET
    media_type: str | Unset = UNSET
    name: str | Unset = UNSET
    total_entry_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_archive_item_readable import AttachmentArchiveItemReadable
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)



        id = self.id

        media_type = self.media_type

        name = self.name

        total_entry_count = self.total_entry_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entries is not UNSET:
            field_dict["entries"] = entries
        if id is not UNSET:
            field_dict["id"] = id
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if name is not UNSET:
            field_dict["name"] = name
        if total_entry_count is not UNSET:
            field_dict["totalEntryCount"] = total_entry_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_archive_item_readable import AttachmentArchiveItemReadable
        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[AttachmentArchiveItemReadable] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = AttachmentArchiveItemReadable.from_dict(entries_item_data)



                entries.append(entries_item)


        id = d.pop("id", UNSET)

        media_type = d.pop("mediaType", UNSET)

        name = d.pop("name", UNSET)

        total_entry_count = d.pop("totalEntryCount", UNSET)

        attachment_archive_metadata_readable = cls(
            entries=entries,
            id=id,
            media_type=media_type,
            name=name,
            total_entry_count=total_entry_count,
        )

        return attachment_archive_metadata_readable

