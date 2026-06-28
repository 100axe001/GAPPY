from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChartHistogramRule")



@_attrs_define
class ChartHistogramRule:
    """ Allows you to organize numeric values in a source data column into buckets of constant size.

        Attributes:
            interval_size (float | Unset): The size of the buckets that are created. Must be positive.
            max_value (float | Unset): The maximum value at which items are placed into buckets. Values greater than the
                maximum are grouped into a single bucket. If omitted, it is determined by the maximum item value.
            min_value (float | Unset): The minimum value at which items are placed into buckets. Values that are less than
                the minimum are grouped into a single bucket. If omitted, it is determined by the minimum item value.
     """

    interval_size: float | Unset = UNSET
    max_value: float | Unset = UNSET
    min_value: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        interval_size = self.interval_size

        max_value = self.max_value

        min_value = self.min_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if interval_size is not UNSET:
            field_dict["intervalSize"] = interval_size
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interval_size = d.pop("intervalSize", UNSET)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        chart_histogram_rule = cls(
            interval_size=interval_size,
            max_value=max_value,
            min_value=min_value,
        )


        chart_histogram_rule.additional_properties = d
        return chart_histogram_rule

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
