from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="SectionColumnProperties")



@_attrs_define
class SectionColumnProperties:
    """ Properties that apply to a section's column.

        Attributes:
            padding_end (Dimension | Unset): A magnitude in a single direction in the specified units.
            width (Dimension | Unset): A magnitude in a single direction in the specified units.
     """

    padding_end: Dimension | Unset = UNSET
    width: Dimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        padding_end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding_end, Unset):
            padding_end = self.padding_end.to_dict()

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if padding_end is not UNSET:
            field_dict["paddingEnd"] = padding_end
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _padding_end = d.pop("paddingEnd", UNSET)
        padding_end: Dimension | Unset
        if isinstance(_padding_end,  Unset):
            padding_end = UNSET
        else:
            padding_end = Dimension.from_dict(_padding_end)




        _width = d.pop("width", UNSET)
        width: Dimension | Unset
        if isinstance(_width,  Unset):
            width = UNSET
        else:
            width = Dimension.from_dict(_width)




        section_column_properties = cls(
            padding_end=padding_end,
            width=width,
        )


        section_column_properties.additional_properties = d
        return section_column_properties

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
