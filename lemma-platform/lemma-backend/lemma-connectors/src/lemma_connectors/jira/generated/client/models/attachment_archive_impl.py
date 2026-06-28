from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.attachment_archive_entry import AttachmentArchiveEntry





T = TypeVar("T", bound="AttachmentArchiveImpl")



@_attrs_define
class AttachmentArchiveImpl:
    """ 
        Attributes:
            entries (list[AttachmentArchiveEntry] | Unset): The list of the items included in the archive.
            total_entry_count (int | Unset): The number of items in the archive.
     """

    entries: list[AttachmentArchiveEntry] | Unset = UNSET
    total_entry_count: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_archive_entry import AttachmentArchiveEntry
        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)



        total_entry_count = self.total_entry_count


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if entries is not UNSET:
            field_dict["entries"] = entries
        if total_entry_count is not UNSET:
            field_dict["totalEntryCount"] = total_entry_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_archive_entry import AttachmentArchiveEntry
        d = dict(src_dict)
        _entries = d.pop("entries", UNSET)
        entries: list[AttachmentArchiveEntry] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = AttachmentArchiveEntry.from_dict(entries_item_data)



                entries.append(entries_item)


        total_entry_count = d.pop("totalEntryCount", UNSET)

        attachment_archive_impl = cls(
            entries=entries,
            total_entry_count=total_entry_count,
        )

        return attachment_archive_impl

