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





T = TypeVar("T", bound="InsertTextRequest")



@_attrs_define
class InsertTextRequest:
    """ Inserts text at the specified location.

        Attributes:
            end_of_segment_location (EndOfSegmentLocation | Unset): Location at the end of a body, header, footer or
                footnote. The location is immediately before the last newline in the document segment.
            location (Location | Unset): A particular location in the document.
            text (str | Unset): The text to be inserted. Inserting a newline character will implicitly create a new
                Paragraph at that index. The paragraph style of the new paragraph will be copied from the paragraph at the
                current insertion index, including lists and bullets. Text styles for inserted text will be determined
                automatically, generally preserving the styling of neighboring text. In most cases, the text style for the
                inserted text will match the text immediately before the insertion index. Some control characters
                (U+0000-U+0008, U+000C-U+001F) and characters from the Unicode Basic Multilingual Plane Private Use Area
                (U+E000-U+F8FF) will be stripped out of the inserted text.
     """

    end_of_segment_location: EndOfSegmentLocation | Unset = UNSET
    location: Location | Unset = UNSET
    text: str | Unset = UNSET
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

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_of_segment_location is not UNSET:
            field_dict["endOfSegmentLocation"] = end_of_segment_location
        if location is not UNSET:
            field_dict["location"] = location
        if text is not UNSET:
            field_dict["text"] = text

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




        text = d.pop("text", UNSET)

        insert_text_request = cls(
            end_of_segment_location=end_of_segment_location,
            location=location,
            text=text,
        )


        insert_text_request.additional_properties = d
        return insert_text_request

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
