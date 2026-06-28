from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RichLinkProperties")



@_attrs_define
class RichLinkProperties:
    """ Properties specific to a RichLink.

        Attributes:
            mime_type (str | Unset): Output only. The [MIME type](https://developers.google.com/drive/api/v3/mime-types) of
                the RichLink, if there's one (for example, when it's a file in Drive).
            title (str | Unset): Output only. The title of the RichLink as displayed in the link. This title matches the
                title of the linked resource at the time of the insertion or last update of the link. This field is always
                present.
            uri (str | Unset): Output only. The URI to the RichLink. This is always present.
     """

    mime_type: str | Unset = UNSET
    title: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mime_type = self.mime_type

        title = self.title

        uri = self.uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if title is not UNSET:
            field_dict["title"] = title
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mime_type = d.pop("mimeType", UNSET)

        title = d.pop("title", UNSET)

        uri = d.pop("uri", UNSET)

        rich_link_properties = cls(
            mime_type=mime_type,
            title=title,
            uri=uri,
        )


        rich_link_properties.additional_properties = d
        return rich_link_properties

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
