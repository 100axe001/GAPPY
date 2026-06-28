from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.line_style_type import LineStyleType
from ..types import UNSET, Unset






T = TypeVar("T", bound="LineStyle")



@_attrs_define
class LineStyle:
    """ Properties that describe the style of a line.

        Attributes:
            type_ (LineStyleType | Unset): The dash type of the line.
            width (int | Unset): The thickness of the line, in px.
     """

    type_: LineStyleType | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: LineStyleType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = LineStyleType(_type_)




        width = d.pop("width", UNSET)

        line_style = cls(
            type_=type_,
            width=width,
        )


        line_style.additional_properties = d
        return line_style

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
