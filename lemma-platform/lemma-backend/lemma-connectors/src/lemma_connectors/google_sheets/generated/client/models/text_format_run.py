from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.text_format import TextFormat





T = TypeVar("T", bound="TextFormatRun")



@_attrs_define
class TextFormatRun:
    """ A run of a text format. The format of this run continues until the start index of the next run. When updating, all
    fields must be set.

        Attributes:
            format_ (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field isn't
                specified.
            start_index (int | Unset): The character index where this run starts.
     """

    format_: TextFormat | Unset = UNSET
    start_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_format import TextFormat
        format_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        start_index = self.start_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_format import TextFormat
        d = dict(src_dict)
        _format_ = d.pop("format", UNSET)
        format_: TextFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = TextFormat.from_dict(_format_)




        start_index = d.pop("startIndex", UNSET)

        text_format_run = cls(
            format_=format_,
            start_index=start_index,
        )


        text_format_run.additional_properties = d
        return text_format_run

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
