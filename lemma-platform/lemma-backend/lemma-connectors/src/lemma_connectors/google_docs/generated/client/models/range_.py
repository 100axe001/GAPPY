from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Range")



@_attrs_define
class Range:
    """ Specifies a contiguous range of text.

        Attributes:
            end_index (int | Unset): The zero-based end index of this range, exclusive, in UTF-16 code units. In all current
                uses, an end index must be provided. This field is an Int32Value in order to accommodate future use cases with
                open-ended ranges.
            segment_id (str | Unset): The ID of the header, footer, or footnote that this range is contained in. An empty
                segment ID signifies the document's body.
            start_index (int | Unset): The zero-based start index of this range, in UTF-16 code units. In all current uses,
                a start index must be provided. This field is an Int32Value in order to accommodate future use cases with open-
                ended ranges.
     """

    end_index: int | Unset = UNSET
    segment_id: str | Unset = UNSET
    start_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_index = self.end_index

        segment_id = self.segment_id

        start_index = self.start_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if segment_id is not UNSET:
            field_dict["segmentId"] = segment_id
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_index = d.pop("endIndex", UNSET)

        segment_id = d.pop("segmentId", UNSET)

        start_index = d.pop("startIndex", UNSET)

        range_ = cls(
            end_index=end_index,
            segment_id=segment_id,
            start_index=start_index,
        )


        range_.additional_properties = d
        return range_

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
