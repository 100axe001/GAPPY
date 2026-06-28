from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.boolean_rule import BooleanRule
  from ..models.gradient_rule import GradientRule
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="ConditionalFormatRule")



@_attrs_define
class ConditionalFormatRule:
    """ A rule describing a conditional format.

        Attributes:
            boolean_rule (BooleanRule | Unset): A rule that may or may not match, depending on the condition.
            gradient_rule (GradientRule | Unset): A rule that applies a gradient color scale format, based on the
                interpolation points listed. The format of a cell will vary based on its contents as compared to the values of
                the interpolation points.
            ranges (list[GridRange] | Unset): The ranges that are formatted if the condition is true. All the ranges must be
                on the same grid.
     """

    boolean_rule: BooleanRule | Unset = UNSET
    gradient_rule: GradientRule | Unset = UNSET
    ranges: list[GridRange] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_rule import BooleanRule
        from ..models.gradient_rule import GradientRule
        from ..models.grid_range import GridRange
        boolean_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.boolean_rule, Unset):
            boolean_rule = self.boolean_rule.to_dict()

        gradient_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gradient_rule, Unset):
            gradient_rule = self.gradient_rule.to_dict()

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if boolean_rule is not UNSET:
            field_dict["booleanRule"] = boolean_rule
        if gradient_rule is not UNSET:
            field_dict["gradientRule"] = gradient_rule
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_rule import BooleanRule
        from ..models.gradient_rule import GradientRule
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        _boolean_rule = d.pop("booleanRule", UNSET)
        boolean_rule: BooleanRule | Unset
        if isinstance(_boolean_rule,  Unset):
            boolean_rule = UNSET
        else:
            boolean_rule = BooleanRule.from_dict(_boolean_rule)




        _gradient_rule = d.pop("gradientRule", UNSET)
        gradient_rule: GradientRule | Unset
        if isinstance(_gradient_rule,  Unset):
            gradient_rule = UNSET
        else:
            gradient_rule = GradientRule.from_dict(_gradient_rule)




        _ranges = d.pop("ranges", UNSET)
        ranges: list[GridRange] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = GridRange.from_dict(ranges_item_data)



                ranges.append(ranges_item)


        conditional_format_rule = cls(
            boolean_rule=boolean_rule,
            gradient_rule=gradient_rule,
            ranges=ranges,
        )


        conditional_format_rule.additional_properties = d
        return conditional_format_rule

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
