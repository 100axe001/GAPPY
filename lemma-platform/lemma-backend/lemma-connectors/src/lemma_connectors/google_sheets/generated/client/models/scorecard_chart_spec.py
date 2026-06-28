from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.scorecard_chart_spec_aggregate_type import ScorecardChartSpecAggregateType
from ..models.scorecard_chart_spec_number_format_source import ScorecardChartSpecNumberFormatSource
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.baseline_value_format import BaselineValueFormat
  from ..models.chart_custom_number_format_options import ChartCustomNumberFormatOptions
  from ..models.chart_data import ChartData
  from ..models.key_value_format import KeyValueFormat





T = TypeVar("T", bound="ScorecardChartSpec")



@_attrs_define
class ScorecardChartSpec:
    """ A scorecard chart. Scorecard charts are used to highlight key performance indicators, known as KPIs, on the
    spreadsheet. A scorecard chart can represent things like total sales, average cost, or a top selling item. You can
    specify a single data value, or aggregate over a range of data. Percentage or absolute difference from a baseline
    value can be highlighted, like changes over time.

        Attributes:
            aggregate_type (ScorecardChartSpecAggregateType | Unset): The aggregation type for key and baseline chart data
                in scorecard chart. This field is not supported for data source charts. Use the ChartData.aggregateType field of
                the key_value_data or baseline_value_data instead for data source charts. This field is optional.
            baseline_value_data (ChartData | Unset): The data included in a domain or series.
            baseline_value_format (BaselineValueFormat | Unset): Formatting options for baseline value.
            custom_format_options (ChartCustomNumberFormatOptions | Unset): Custom number formatting options for chart
                attributes.
            key_value_data (ChartData | Unset): The data included in a domain or series.
            key_value_format (KeyValueFormat | Unset): Formatting options for key value.
            number_format_source (ScorecardChartSpecNumberFormatSource | Unset): The number format source used in the
                scorecard chart. This field is optional.
            scale_factor (float | Unset): Value to scale scorecard key and baseline value. For example, a factor of 10 can
                be used to divide all values in the chart by 10. This field is optional.
     """

    aggregate_type: ScorecardChartSpecAggregateType | Unset = UNSET
    baseline_value_data: ChartData | Unset = UNSET
    baseline_value_format: BaselineValueFormat | Unset = UNSET
    custom_format_options: ChartCustomNumberFormatOptions | Unset = UNSET
    key_value_data: ChartData | Unset = UNSET
    key_value_format: KeyValueFormat | Unset = UNSET
    number_format_source: ScorecardChartSpecNumberFormatSource | Unset = UNSET
    scale_factor: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.baseline_value_format import BaselineValueFormat
        from ..models.chart_custom_number_format_options import ChartCustomNumberFormatOptions
        from ..models.chart_data import ChartData
        from ..models.key_value_format import KeyValueFormat
        aggregate_type: str | Unset = UNSET
        if not isinstance(self.aggregate_type, Unset):
            aggregate_type = self.aggregate_type.value


        baseline_value_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline_value_data, Unset):
            baseline_value_data = self.baseline_value_data.to_dict()

        baseline_value_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.baseline_value_format, Unset):
            baseline_value_format = self.baseline_value_format.to_dict()

        custom_format_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_format_options, Unset):
            custom_format_options = self.custom_format_options.to_dict()

        key_value_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_value_data, Unset):
            key_value_data = self.key_value_data.to_dict()

        key_value_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_value_format, Unset):
            key_value_format = self.key_value_format.to_dict()

        number_format_source: str | Unset = UNSET
        if not isinstance(self.number_format_source, Unset):
            number_format_source = self.number_format_source.value


        scale_factor = self.scale_factor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aggregate_type is not UNSET:
            field_dict["aggregateType"] = aggregate_type
        if baseline_value_data is not UNSET:
            field_dict["baselineValueData"] = baseline_value_data
        if baseline_value_format is not UNSET:
            field_dict["baselineValueFormat"] = baseline_value_format
        if custom_format_options is not UNSET:
            field_dict["customFormatOptions"] = custom_format_options
        if key_value_data is not UNSET:
            field_dict["keyValueData"] = key_value_data
        if key_value_format is not UNSET:
            field_dict["keyValueFormat"] = key_value_format
        if number_format_source is not UNSET:
            field_dict["numberFormatSource"] = number_format_source
        if scale_factor is not UNSET:
            field_dict["scaleFactor"] = scale_factor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.baseline_value_format import BaselineValueFormat
        from ..models.chart_custom_number_format_options import ChartCustomNumberFormatOptions
        from ..models.chart_data import ChartData
        from ..models.key_value_format import KeyValueFormat
        d = dict(src_dict)
        _aggregate_type = d.pop("aggregateType", UNSET)
        aggregate_type: ScorecardChartSpecAggregateType | Unset
        if isinstance(_aggregate_type,  Unset):
            aggregate_type = UNSET
        else:
            aggregate_type = ScorecardChartSpecAggregateType(_aggregate_type)




        _baseline_value_data = d.pop("baselineValueData", UNSET)
        baseline_value_data: ChartData | Unset
        if isinstance(_baseline_value_data,  Unset):
            baseline_value_data = UNSET
        else:
            baseline_value_data = ChartData.from_dict(_baseline_value_data)




        _baseline_value_format = d.pop("baselineValueFormat", UNSET)
        baseline_value_format: BaselineValueFormat | Unset
        if isinstance(_baseline_value_format,  Unset):
            baseline_value_format = UNSET
        else:
            baseline_value_format = BaselineValueFormat.from_dict(_baseline_value_format)




        _custom_format_options = d.pop("customFormatOptions", UNSET)
        custom_format_options: ChartCustomNumberFormatOptions | Unset
        if isinstance(_custom_format_options,  Unset):
            custom_format_options = UNSET
        else:
            custom_format_options = ChartCustomNumberFormatOptions.from_dict(_custom_format_options)




        _key_value_data = d.pop("keyValueData", UNSET)
        key_value_data: ChartData | Unset
        if isinstance(_key_value_data,  Unset):
            key_value_data = UNSET
        else:
            key_value_data = ChartData.from_dict(_key_value_data)




        _key_value_format = d.pop("keyValueFormat", UNSET)
        key_value_format: KeyValueFormat | Unset
        if isinstance(_key_value_format,  Unset):
            key_value_format = UNSET
        else:
            key_value_format = KeyValueFormat.from_dict(_key_value_format)




        _number_format_source = d.pop("numberFormatSource", UNSET)
        number_format_source: ScorecardChartSpecNumberFormatSource | Unset
        if isinstance(_number_format_source,  Unset):
            number_format_source = UNSET
        else:
            number_format_source = ScorecardChartSpecNumberFormatSource(_number_format_source)




        scale_factor = d.pop("scaleFactor", UNSET)

        scorecard_chart_spec = cls(
            aggregate_type=aggregate_type,
            baseline_value_data=baseline_value_data,
            baseline_value_format=baseline_value_format,
            custom_format_options=custom_format_options,
            key_value_data=key_value_data,
            key_value_format=key_value_format,
            number_format_source=number_format_source,
            scale_factor=scale_factor,
        )


        scorecard_chart_spec.additional_properties = d
        return scorecard_chart_spec

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
