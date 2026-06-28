from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.optional_color import OptionalColor





T = TypeVar("T", bound="Background")



@_attrs_define
class Background:
    """ Represents the background of a document.

        Attributes:
            color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
     """

    color: OptionalColor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.optional_color import OptionalColor
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.optional_color import OptionalColor
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: OptionalColor | Unset
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = OptionalColor.from_dict(_color)




        background = cls(
            color=color,
        )


        background.additional_properties = d
        return background

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
