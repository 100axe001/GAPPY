from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Link")



@_attrs_define
class Link:
    """ A reference to another portion of a document or an external URL resource.

        Attributes:
            bookmark_id (str | Unset): The ID of a bookmark in this document.
            heading_id (str | Unset): The ID of a heading in this document.
            url (str | Unset): An external URL.
     """

    bookmark_id: str | Unset = UNSET
    heading_id: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bookmark_id = self.bookmark_id

        heading_id = self.heading_id

        url = self.url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bookmark_id is not UNSET:
            field_dict["bookmarkId"] = bookmark_id
        if heading_id is not UNSET:
            field_dict["headingId"] = heading_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bookmark_id = d.pop("bookmarkId", UNSET)

        heading_id = d.pop("headingId", UNSET)

        url = d.pop("url", UNSET)

        link = cls(
            bookmark_id=bookmark_id,
            heading_id=heading_id,
            url=url,
        )


        link.additional_properties = d
        return link

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
