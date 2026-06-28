from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.nesting_level import NestingLevel





T = TypeVar("T", bound="ListProperties")



@_attrs_define
class ListProperties:
    """ The properties of a list that describe the look and feel of bullets belonging to paragraphs associated with a list.

        Attributes:
            nesting_levels (list[NestingLevel] | Unset): Describes the properties of the bullets at the associated level. A
                list has at most 9 levels of nesting with nesting level 0 corresponding to the top-most level and nesting level
                8 corresponding to the most nested level. The nesting levels are returned in ascending order with the least
                nested returned first.
     """

    nesting_levels: list[NestingLevel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.nesting_level import NestingLevel
        nesting_levels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nesting_levels, Unset):
            nesting_levels = []
            for nesting_levels_item_data in self.nesting_levels:
                nesting_levels_item = nesting_levels_item_data.to_dict()
                nesting_levels.append(nesting_levels_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nesting_levels is not UNSET:
            field_dict["nestingLevels"] = nesting_levels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nesting_level import NestingLevel
        d = dict(src_dict)
        _nesting_levels = d.pop("nestingLevels", UNSET)
        nesting_levels: list[NestingLevel] | Unset = UNSET
        if _nesting_levels is not UNSET:
            nesting_levels = []
            for nesting_levels_item_data in _nesting_levels:
                nesting_levels_item = NestingLevel.from_dict(nesting_levels_item_data)



                nesting_levels.append(nesting_levels_item)


        list_properties = cls(
            nesting_levels=nesting_levels,
        )


        list_properties.additional_properties = d
        return list_properties

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
