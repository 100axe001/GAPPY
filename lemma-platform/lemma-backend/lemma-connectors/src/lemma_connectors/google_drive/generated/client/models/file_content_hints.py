from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_content_hints_thumbnail import FileContentHintsThumbnail





T = TypeVar("T", bound="FileContentHints")



@_attrs_define
class FileContentHints:
    """ Additional information about the content of the file. These fields are never populated in responses.

        Attributes:
            indexable_text (str | Unset): Text to be indexed for the file to improve fullText queries. This is limited to
                128 KB in length and might contain HTML elements. For more information, see Manage file metadata.
            thumbnail (FileContentHintsThumbnail | Unset): A thumbnail for the file. This will only be used if Google Drive
                cannot generate a standard thumbnail.
     """

    indexable_text: str | Unset = UNSET
    thumbnail: FileContentHintsThumbnail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_content_hints_thumbnail import FileContentHintsThumbnail
        indexable_text = self.indexable_text

        thumbnail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if indexable_text is not UNSET:
            field_dict["indexableText"] = indexable_text
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_content_hints_thumbnail import FileContentHintsThumbnail
        d = dict(src_dict)
        indexable_text = d.pop("indexableText", UNSET)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: FileContentHintsThumbnail | Unset
        if isinstance(_thumbnail,  Unset):
            thumbnail = UNSET
        else:
            thumbnail = FileContentHintsThumbnail.from_dict(_thumbnail)




        file_content_hints = cls(
            indexable_text=indexable_text,
            thumbnail=thumbnail,
        )


        file_content_hints.additional_properties = d
        return file_content_hints

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
