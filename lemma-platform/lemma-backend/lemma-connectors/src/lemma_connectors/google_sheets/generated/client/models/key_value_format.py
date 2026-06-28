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
  from ..models.text_position import TextPosition





T = TypeVar("T", bound="KeyValueFormat")



@_attrs_define
class KeyValueFormat:
    """ Formatting options for key value.

        Attributes:
            position (TextPosition | Unset): Position settings for text.
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
     """

    position: TextPosition | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if position is not UNSET:
            field_dict["position"] = position
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        d = dict(src_dict)
        _position = d.pop("position", UNSET)
        position: TextPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = TextPosition.from_dict(_position)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        key_value_format = cls(
            position=position,
            text_format=text_format,
        )


        key_value_format.additional_properties = d
        return key_value_format

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
