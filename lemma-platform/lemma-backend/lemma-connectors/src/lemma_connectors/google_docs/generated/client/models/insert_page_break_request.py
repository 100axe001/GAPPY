from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.end_of_segment_location import EndOfSegmentLocation
  from ..models.location import Location





T = TypeVar("T", bound="InsertPageBreakRequest")



@_attrs_define
class InsertPageBreakRequest:
    """ Inserts a page break followed by a newline at the specified location.

        Attributes:
            end_of_segment_location (EndOfSegmentLocation | Unset): Location at the end of a body, header, footer or
                footnote. The location is immediately before the last newline in the document segment.
            location (Location | Unset): A particular location in the document.
     """

    end_of_segment_location: EndOfSegmentLocation | Unset = UNSET
    location: Location | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.end_of_segment_location import EndOfSegmentLocation
        from ..models.location import Location
        end_of_segment_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_of_segment_location, Unset):
            end_of_segment_location = self.end_of_segment_location.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_of_segment_location is not UNSET:
            field_dict["endOfSegmentLocation"] = end_of_segment_location
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.end_of_segment_location import EndOfSegmentLocation
        from ..models.location import Location
        d = dict(src_dict)
        _end_of_segment_location = d.pop("endOfSegmentLocation", UNSET)
        end_of_segment_location: EndOfSegmentLocation | Unset
        if isinstance(_end_of_segment_location,  Unset):
            end_of_segment_location = UNSET
        else:
            end_of_segment_location = EndOfSegmentLocation.from_dict(_end_of_segment_location)




        _location = d.pop("location", UNSET)
        location: Location | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)




        insert_page_break_request = cls(
            end_of_segment_location=end_of_segment_location,
            location=location,
        )


        insert_page_break_request.additional_properties = d
        return insert_page_break_request

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
