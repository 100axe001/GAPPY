from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chart_date_time_rule_type import ChartDateTimeRuleType
from ..types import UNSET, Unset






T = TypeVar("T", bound="ChartDateTimeRule")



@_attrs_define
class ChartDateTimeRule:
    """ Allows you to organize the date-time values in a source data column into buckets based on selected parts of their
    date or time values.

        Attributes:
            type_ (ChartDateTimeRuleType | Unset): The type of date-time grouping to apply.
     """

    type_: ChartDateTimeRuleType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ChartDateTimeRuleType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ChartDateTimeRuleType(_type_)




        chart_date_time_rule = cls(
            type_=type_,
        )


        chart_date_time_rule.additional_properties = d
        return chart_date_time_rule

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
