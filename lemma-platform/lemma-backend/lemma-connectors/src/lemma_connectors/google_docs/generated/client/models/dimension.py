from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dimension_unit import DimensionUnit
from ..types import UNSET, Unset






T = TypeVar("T", bound="Dimension")



@_attrs_define
class Dimension:
    """ A magnitude in a single direction in the specified units.

        Attributes:
            magnitude (float | Unset): The magnitude.
            unit (DimensionUnit | Unset): The units for magnitude.
     """

    magnitude: float | Unset = UNSET
    unit: DimensionUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        magnitude = self.magnitude

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if magnitude is not UNSET:
            field_dict["magnitude"] = magnitude
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        magnitude = d.pop("magnitude", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: DimensionUnit | Unset
        if isinstance(_unit,  Unset):
            unit = UNSET
        else:
            unit = DimensionUnit(_unit)




        dimension = cls(
            magnitude=magnitude,
            unit=unit,
        )


        dimension.additional_properties = d
        return dimension

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
