from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="HistogramRule")



@_attrs_define
class HistogramRule:
    """ Allows you to organize the numeric values in a source data column into buckets of a constant size. All values from
    HistogramRule.start to HistogramRule.end are placed into groups of size HistogramRule.interval. In addition, all
    values below HistogramRule.start are placed in one group, and all values above HistogramRule.end are placed in
    another. Only HistogramRule.interval is required, though if HistogramRule.start and HistogramRule.end are both
    provided, HistogramRule.start must be less than HistogramRule.end. For example, a pivot table showing average
    purchase amount by age that has 50+ rows: +-----+-------------------+ | Age | AVERAGE of Amount |
    +-----+-------------------+ | 16 | $27.13 | | 17 | $5.24 | | 18 | $20.15 | ... +-----+-------------------+ could be
    turned into a pivot table that looks like the one below by applying a histogram group rule with a
    HistogramRule.start of 25, an HistogramRule.interval of 20, and an HistogramRule.end of 65.
    +-------------+-------------------+ | Grouped Age | AVERAGE of Amount | +-------------+-------------------+ | < 25 |
    $19.34 | | 25-45 | $31.43 | | 45-65 | $35.87 | | > 65 | $27.55 | +-------------+-------------------+ | Grand Total |
    $29.12 | +-------------+-------------------+

        Attributes:
            end (float | Unset): The maximum value at which items are placed into buckets of constant size. Values above end
                are lumped into a single bucket. This field is optional.
            interval (float | Unset): The size of the buckets that are created. Must be positive.
            start (float | Unset): The minimum value at which items are placed into buckets of constant size. Values below
                start are lumped into a single bucket. This field is optional.
     """

    end: float | Unset = UNSET
    interval: float | Unset = UNSET
    start: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end = self.end

        interval = self.interval

        start = self.start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end is not UNSET:
            field_dict["end"] = end
        if interval is not UNSET:
            field_dict["interval"] = interval
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        interval = d.pop("interval", UNSET)

        start = d.pop("start", UNSET)

        histogram_rule = cls(
            end=end,
            interval=interval,
            start=start,
        )


        histogram_rule.additional_properties = d
        return histogram_rule

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
