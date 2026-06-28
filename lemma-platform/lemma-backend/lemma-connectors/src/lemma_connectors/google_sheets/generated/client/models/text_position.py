from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.text_position_horizontal_alignment import TextPositionHorizontalAlignment
from ..types import UNSET, Unset






T = TypeVar("T", bound="TextPosition")



@_attrs_define
class TextPosition:
    """ Position settings for text.

        Attributes:
            horizontal_alignment (TextPositionHorizontalAlignment | Unset): Horizontal alignment setting for the piece of
                text.
     """

    horizontal_alignment: TextPositionHorizontalAlignment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        horizontal_alignment: str | Unset = UNSET
        if not isinstance(self.horizontal_alignment, Unset):
            horizontal_alignment = self.horizontal_alignment.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if horizontal_alignment is not UNSET:
            field_dict["horizontalAlignment"] = horizontal_alignment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _horizontal_alignment = d.pop("horizontalAlignment", UNSET)
        horizontal_alignment: TextPositionHorizontalAlignment | Unset
        if isinstance(_horizontal_alignment,  Unset):
            horizontal_alignment = UNSET
        else:
            horizontal_alignment = TextPositionHorizontalAlignment(_horizontal_alignment)




        text_position = cls(
            horizontal_alignment=horizontal_alignment,
        )


        text_position.additional_properties = d
        return text_position

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
