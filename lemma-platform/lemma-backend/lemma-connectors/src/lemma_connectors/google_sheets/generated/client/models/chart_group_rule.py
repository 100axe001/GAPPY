from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_date_time_rule import ChartDateTimeRule
  from ..models.chart_histogram_rule import ChartHistogramRule





T = TypeVar("T", bound="ChartGroupRule")



@_attrs_define
class ChartGroupRule:
    """ An optional setting on the ChartData of the domain of a data source chart that defines buckets for the values in the
    domain rather than breaking out each individual value. For example, when plotting a data source chart, you can
    specify a histogram rule on the domain (it should only contain numeric values), grouping its values into buckets.
    Any values of a chart series that fall into the same bucket are aggregated based on the aggregate_type.

        Attributes:
            date_time_rule (ChartDateTimeRule | Unset): Allows you to organize the date-time values in a source data column
                into buckets based on selected parts of their date or time values.
            histogram_rule (ChartHistogramRule | Unset): Allows you to organize numeric values in a source data column into
                buckets of constant size.
     """

    date_time_rule: ChartDateTimeRule | Unset = UNSET
    histogram_rule: ChartHistogramRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_date_time_rule import ChartDateTimeRule
        from ..models.chart_histogram_rule import ChartHistogramRule
        date_time_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_time_rule, Unset):
            date_time_rule = self.date_time_rule.to_dict()

        histogram_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.histogram_rule, Unset):
            histogram_rule = self.histogram_rule.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date_time_rule is not UNSET:
            field_dict["dateTimeRule"] = date_time_rule
        if histogram_rule is not UNSET:
            field_dict["histogramRule"] = histogram_rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_date_time_rule import ChartDateTimeRule
        from ..models.chart_histogram_rule import ChartHistogramRule
        d = dict(src_dict)
        _date_time_rule = d.pop("dateTimeRule", UNSET)
        date_time_rule: ChartDateTimeRule | Unset
        if isinstance(_date_time_rule,  Unset):
            date_time_rule = UNSET
        else:
            date_time_rule = ChartDateTimeRule.from_dict(_date_time_rule)




        _histogram_rule = d.pop("histogramRule", UNSET)
        histogram_rule: ChartHistogramRule | Unset
        if isinstance(_histogram_rule,  Unset):
            histogram_rule = UNSET
        else:
            histogram_rule = ChartHistogramRule.from_dict(_histogram_rule)




        chart_group_rule = cls(
            date_time_rule=date_time_rule,
            histogram_rule=histogram_rule,
        )


        chart_group_rule.additional_properties = d
        return chart_group_rule

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
