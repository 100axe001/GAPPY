from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.boolean_condition import BooleanCondition





T = TypeVar("T", bound="PivotFilterCriteria")



@_attrs_define
class PivotFilterCriteria:
    """ Criteria for showing/hiding rows in a pivot table.

        Attributes:
            condition (BooleanCondition | Unset): A condition that can evaluate to true or false. BooleanConditions are used
                by conditional formatting, data validation, and the criteria in filters.
            visible_by_default (bool | Unset): Whether values are visible by default. If true, the visible_values are
                ignored, all values that meet condition (if specified) are shown. If false, values that are both in
                visible_values and meet condition are shown.
            visible_values (list[str] | Unset): Values that should be included. Values not listed here are excluded.
     """

    condition: BooleanCondition | Unset = UNSET
    visible_by_default: bool | Unset = UNSET
    visible_values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_condition import BooleanCondition
        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        visible_by_default = self.visible_by_default

        visible_values: list[str] | Unset = UNSET
        if not isinstance(self.visible_values, Unset):
            visible_values = self.visible_values




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition is not UNSET:
            field_dict["condition"] = condition
        if visible_by_default is not UNSET:
            field_dict["visibleByDefault"] = visible_by_default
        if visible_values is not UNSET:
            field_dict["visibleValues"] = visible_values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boolean_condition import BooleanCondition
        d = dict(src_dict)
        _condition = d.pop("condition", UNSET)
        condition: BooleanCondition | Unset
        if isinstance(_condition,  Unset):
            condition = UNSET
        else:
            condition = BooleanCondition.from_dict(_condition)




        visible_by_default = d.pop("visibleByDefault", UNSET)

        visible_values = cast(list[str], d.pop("visibleValues", UNSET))


        pivot_filter_criteria = cls(
            condition=condition,
            visible_by_default=visible_by_default,
            visible_values=visible_values,
        )


        pivot_filter_criteria.additional_properties = d
        return pivot_filter_criteria

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
