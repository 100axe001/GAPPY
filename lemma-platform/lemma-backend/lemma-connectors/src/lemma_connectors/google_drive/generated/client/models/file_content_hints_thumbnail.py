from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileContentHintsThumbnail")



@_attrs_define
class FileContentHintsThumbnail:
    """ A thumbnail for the file. This will only be used if Google Drive cannot generate a standard thumbnail.

        Attributes:
            image (str | Unset): The thumbnail data encoded with URL-safe Base64 (RFC 4648 section 5).
            mime_type (str | Unset): The MIME type of the thumbnail.
     """

    image: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image = self.image

        mime_type = self.mime_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image is not UNSET:
            field_dict["image"] = image
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image = d.pop("image", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        file_content_hints_thumbnail = cls(
            image=image,
            mime_type=mime_type,
        )


        file_content_hints_thumbnail.additional_properties = d
        return file_content_hints_thumbnail

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
