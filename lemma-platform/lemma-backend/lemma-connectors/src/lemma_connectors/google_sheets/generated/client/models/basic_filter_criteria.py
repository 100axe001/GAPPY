from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.filter_criteria import FilterCriteria





T = TypeVar("T", bound="BasicFilterCriteria")



@_attrs_define
class BasicFilterCriteria:
    """ The criteria for showing/hiding values per column. The map's key is the column index, and the value is the criteria
    for that column. This field is deprecated in favor of filter_specs.

     """

    additional_properties: dict[str, FilterCriteria] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_criteria import FilterCriteria
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_criteria import FilterCriteria
        d = dict(src_dict)
        basic_filter_criteria = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FilterCriteria.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        basic_filter_criteria.additional_properties = additional_properties
        return basic_filter_criteria

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FilterCriteria:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FilterCriteria) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
