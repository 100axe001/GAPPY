from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Location")



@_attrs_define
class Location:
    """ A particular location in the document.

        Attributes:
            index (int | Unset): The zero-based index, in UTF-16 code units. The index is relative to the beginning of the
                segment specified by segment_id.
            segment_id (str | Unset): The ID of the header, footer or footnote the location is in. An empty segment ID
                signifies the document's body.
     """

    index: int | Unset = UNSET
    segment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        index = self.index

        segment_id = self.segment_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        segment_id = d.pop("segmentId", UNSET)

        location = cls(
            index=index,
            segment_id=segment_id,
        )


        location.additional_properties = d
        return location

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
