from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.date_time_rule_type import DateTimeRuleType
from ..types import UNSET, Unset






T = TypeVar("T", bound="DateTimeRule")



@_attrs_define
class DateTimeRule:
    """ Allows you to organize the date-time values in a source data column into buckets based on selected parts of their
    date or time values. For example, consider a pivot table showing sales transactions by date:
    +----------+--------------+ | Date | SUM of Sales | +----------+--------------+ | 1/1/2017 | $621.14 | | 2/3/2017 |
    $708.84 | | 5/8/2017 | $326.84 | ... +----------+--------------+ Applying a date-time group rule with a
    DateTimeRuleType of YEAR_MONTH results in the following pivot table. +--------------+--------------+ | Grouped Date
    | SUM of Sales | +--------------+--------------+ | 2017-Jan | $53,731.78 | | 2017-Feb | $83,475.32 | | 2017-Mar |
    $94,385.05 | ... +--------------+--------------+

        Attributes:
            type_ (DateTimeRuleType | Unset): The type of date-time grouping to apply.
     """

    type_: DateTimeRuleType | Unset = UNSET
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
        type_: DateTimeRuleType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = DateTimeRuleType(_type_)




        date_time_rule = cls(
            type_=type_,
        )


        date_time_rule.additional_properties = d
        return date_time_rule

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
