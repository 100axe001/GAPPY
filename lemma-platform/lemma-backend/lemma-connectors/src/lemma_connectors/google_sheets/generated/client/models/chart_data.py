from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chart_data_aggregate_type import ChartDataAggregateType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_group_rule import ChartGroupRule
  from ..models.chart_source_range import ChartSourceRange
  from ..models.data_source_column_reference import DataSourceColumnReference





T = TypeVar("T", bound="ChartData")



@_attrs_define
class ChartData:
    """ The data included in a domain or series.

        Attributes:
            aggregate_type (ChartDataAggregateType | Unset): The aggregation type for the series of a data source chart.
                Only supported for data source charts.
            column_reference (DataSourceColumnReference | Unset): An unique identifier that references a data source column.
            group_rule (ChartGroupRule | Unset): An optional setting on the ChartData of the domain of a data source chart
                that defines buckets for the values in the domain rather than breaking out each individual value. For example,
                when plotting a data source chart, you can specify a histogram rule on the domain (it should only contain
                numeric values), grouping its values into buckets. Any values of a chart series that fall into the same bucket
                are aggregated based on the aggregate_type.
            source_range (ChartSourceRange | Unset): Source ranges for a chart.
     """

    aggregate_type: ChartDataAggregateType | Unset = UNSET
    column_reference: DataSourceColumnReference | Unset = UNSET
    group_rule: ChartGroupRule | Unset = UNSET
    source_range: ChartSourceRange | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_group_rule import ChartGroupRule
        from ..models.chart_source_range import ChartSourceRange
        from ..models.data_source_column_reference import DataSourceColumnReference
        aggregate_type: str | Unset = UNSET
        if not isinstance(self.aggregate_type, Unset):
            aggregate_type = self.aggregate_type.value


        column_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_reference, Unset):
            column_reference = self.column_reference.to_dict()

        group_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_rule, Unset):
            group_rule = self.group_rule.to_dict()

        source_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_range, Unset):
            source_range = self.source_range.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aggregate_type is not UNSET:
            field_dict["aggregateType"] = aggregate_type
        if column_reference is not UNSET:
            field_dict["columnReference"] = column_reference
        if group_rule is not UNSET:
            field_dict["groupRule"] = group_rule
        if source_range is not UNSET:
            field_dict["sourceRange"] = source_range

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_group_rule import ChartGroupRule
        from ..models.chart_source_range import ChartSourceRange
        from ..models.data_source_column_reference import DataSourceColumnReference
        d = dict(src_dict)
        _aggregate_type = d.pop("aggregateType", UNSET)
        aggregate_type: ChartDataAggregateType | Unset
        if isinstance(_aggregate_type,  Unset):
            aggregate_type = UNSET
        else:
            aggregate_type = ChartDataAggregateType(_aggregate_type)




        _column_reference = d.pop("columnReference", UNSET)
        column_reference: DataSourceColumnReference | Unset
        if isinstance(_column_reference,  Unset):
            column_reference = UNSET
        else:
            column_reference = DataSourceColumnReference.from_dict(_column_reference)




        _group_rule = d.pop("groupRule", UNSET)
        group_rule: ChartGroupRule | Unset
        if isinstance(_group_rule,  Unset):
            group_rule = UNSET
        else:
            group_rule = ChartGroupRule.from_dict(_group_rule)




        _source_range = d.pop("sourceRange", UNSET)
        source_range: ChartSourceRange | Unset
        if isinstance(_source_range,  Unset):
            source_range = UNSET
        else:
            source_range = ChartSourceRange.from_dict(_source_range)




        chart_data = cls(
            aggregate_type=aggregate_type,
            column_reference=column_reference,
            group_rule=group_rule,
            source_range=source_range,
        )


        chart_data.additional_properties = d
        return chart_data

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
