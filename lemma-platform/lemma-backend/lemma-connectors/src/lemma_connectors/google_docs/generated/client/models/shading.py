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





T = TypeVar("T", bound="Shading")



@_attrs_define
class Shading:
    """ The shading of a paragraph.

        Attributes:
            background_color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
     """

    background_color: OptionalColor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.optional_color import OptionalColor
        background_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_color, Unset):
            background_color = self.background_color.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.optional_color import OptionalColor
        d = dict(src_dict)
        _background_color = d.pop("backgroundColor", UNSET)
        background_color: OptionalColor | Unset
        if isinstance(_background_color,  Unset):
            background_color = UNSET
        else:
            background_color = OptionalColor.from_dict(_background_color)




        shading = cls(
            background_color=background_color,
        )


        shading.additional_properties = d
        return shading

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
