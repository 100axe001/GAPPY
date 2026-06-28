from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.basic_chart_spec_chart_type import BasicChartSpecChartType
from ..models.basic_chart_spec_compare_mode import BasicChartSpecCompareMode
from ..models.basic_chart_spec_legend_position import BasicChartSpecLegendPosition
from ..models.basic_chart_spec_stacked_type import BasicChartSpecStackedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.basic_chart_axis import BasicChartAxis
  from ..models.basic_chart_domain import BasicChartDomain
  from ..models.basic_chart_series import BasicChartSeries
  from ..models.data_label import DataLabel





T = TypeVar("T", bound="BasicChartSpec")



@_attrs_define
class BasicChartSpec:
    """ The specification for a basic chart. See BasicChartType for the list of charts this supports.

        Attributes:
            axis (list[BasicChartAxis] | Unset): The axis on the chart.
            chart_type (BasicChartSpecChartType | Unset): The type of the chart.
            compare_mode (BasicChartSpecCompareMode | Unset): The behavior of tooltips and data highlighting when hovering
                on data and chart area.
            domains (list[BasicChartDomain] | Unset): The domain of data this is charting. Only a single domain is
                supported.
            header_count (int | Unset): The number of rows or columns in the data that are "headers". If not set, Google
                Sheets will guess how many rows are headers based on the data. (Note that BasicChartAxis.title may override the
                axis title inferred from the header values.)
            interpolate_nulls (bool | Unset): If some values in a series are missing, gaps may appear in the chart (e.g,
                segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line,
                Area, and Combo charts.
            legend_position (BasicChartSpecLegendPosition | Unset): The position of the chart legend.
            line_smoothing (bool | Unset): Gets whether all lines should be rendered smooth or straight by default. Applies
                to Line charts.
            series (list[BasicChartSeries] | Unset): The data this chart is visualizing.
            stacked_type (BasicChartSpecStackedType | Unset): The stacked type for charts that support vertical stacking.
                Applies to Area, Bar, Column, Combo, and Stepped Area charts.
            three_dimensional (bool | Unset): True to make the chart 3D. Applies to Bar and Column charts.
            total_data_label (DataLabel | Unset): Settings for one set of data labels. Data labels are annotations that
                appear next to a set of data, such as the points on a line chart, and provide additional information about what
                the data represents, such as a text representation of the value behind that point on the graph.
     """

    axis: list[BasicChartAxis] | Unset = UNSET
    chart_type: BasicChartSpecChartType | Unset = UNSET
    compare_mode: BasicChartSpecCompareMode | Unset = UNSET
    domains: list[BasicChartDomain] | Unset = UNSET
    header_count: int | Unset = UNSET
    interpolate_nulls: bool | Unset = UNSET
    legend_position: BasicChartSpecLegendPosition | Unset = UNSET
    line_smoothing: bool | Unset = UNSET
    series: list[BasicChartSeries] | Unset = UNSET
    stacked_type: BasicChartSpecStackedType | Unset = UNSET
    three_dimensional: bool | Unset = UNSET
    total_data_label: DataLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_chart_axis import BasicChartAxis
        from ..models.basic_chart_domain import BasicChartDomain
        from ..models.basic_chart_series import BasicChartSeries
        from ..models.data_label import DataLabel
        axis: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.axis, Unset):
            axis = []
            for axis_item_data in self.axis:
                axis_item = axis_item_data.to_dict()
                axis.append(axis_item)



        chart_type: str | Unset = UNSET
        if not isinstance(self.chart_type, Unset):
            chart_type = self.chart_type.value


        compare_mode: str | Unset = UNSET
        if not isinstance(self.compare_mode, Unset):
            compare_mode = self.compare_mode.value


        domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)



        header_count = self.header_count

        interpolate_nulls = self.interpolate_nulls

        legend_position: str | Unset = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value


        line_smoothing = self.line_smoothing

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)



        stacked_type: str | Unset = UNSET
        if not isinstance(self.stacked_type, Unset):
            stacked_type = self.stacked_type.value


        three_dimensional = self.three_dimensional

        total_data_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_data_label, Unset):
            total_data_label = self.total_data_label.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if axis is not UNSET:
            field_dict["axis"] = axis
        if chart_type is not UNSET:
            field_dict["chartType"] = chart_type
        if compare_mode is not UNSET:
            field_dict["compareMode"] = compare_mode
        if domains is not UNSET:
            field_dict["domains"] = domains
        if header_count is not UNSET:
            field_dict["headerCount"] = header_count
        if interpolate_nulls is not UNSET:
            field_dict["interpolateNulls"] = interpolate_nulls
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if line_smoothing is not UNSET:
            field_dict["lineSmoothing"] = line_smoothing
        if series is not UNSET:
            field_dict["series"] = series
        if stacked_type is not UNSET:
            field_dict["stackedType"] = stacked_type
        if three_dimensional is not UNSET:
            field_dict["threeDimensional"] = three_dimensional
        if total_data_label is not UNSET:
            field_dict["totalDataLabel"] = total_data_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_chart_axis import BasicChartAxis
        from ..models.basic_chart_domain import BasicChartDomain
        from ..models.basic_chart_series import BasicChartSeries
        from ..models.data_label import DataLabel
        d = dict(src_dict)
        _axis = d.pop("axis", UNSET)
        axis: list[BasicChartAxis] | Unset = UNSET
        if _axis is not UNSET:
            axis = []
            for axis_item_data in _axis:
                axis_item = BasicChartAxis.from_dict(axis_item_data)



                axis.append(axis_item)


        _chart_type = d.pop("chartType", UNSET)
        chart_type: BasicChartSpecChartType | Unset
        if isinstance(_chart_type,  Unset):
            chart_type = UNSET
        else:
            chart_type = BasicChartSpecChartType(_chart_type)




        _compare_mode = d.pop("compareMode", UNSET)
        compare_mode: BasicChartSpecCompareMode | Unset
        if isinstance(_compare_mode,  Unset):
            compare_mode = UNSET
        else:
            compare_mode = BasicChartSpecCompareMode(_compare_mode)




        _domains = d.pop("domains", UNSET)
        domains: list[BasicChartDomain] | Unset = UNSET
        if _domains is not UNSET:
            domains = []
            for domains_item_data in _domains:
                domains_item = BasicChartDomain.from_dict(domains_item_data)



                domains.append(domains_item)


        header_count = d.pop("headerCount", UNSET)

        interpolate_nulls = d.pop("interpolateNulls", UNSET)

        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: BasicChartSpecLegendPosition | Unset
        if isinstance(_legend_position,  Unset):
            legend_position = UNSET
        else:
            legend_position = BasicChartSpecLegendPosition(_legend_position)




        line_smoothing = d.pop("lineSmoothing", UNSET)

        _series = d.pop("series", UNSET)
        series: list[BasicChartSeries] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = BasicChartSeries.from_dict(series_item_data)



                series.append(series_item)


        _stacked_type = d.pop("stackedType", UNSET)
        stacked_type: BasicChartSpecStackedType | Unset
        if isinstance(_stacked_type,  Unset):
            stacked_type = UNSET
        else:
            stacked_type = BasicChartSpecStackedType(_stacked_type)




        three_dimensional = d.pop("threeDimensional", UNSET)

        _total_data_label = d.pop("totalDataLabel", UNSET)
        total_data_label: DataLabel | Unset
        if isinstance(_total_data_label,  Unset):
            total_data_label = UNSET
        else:
            total_data_label = DataLabel.from_dict(_total_data_label)




        basic_chart_spec = cls(
            axis=axis,
            chart_type=chart_type,
            compare_mode=compare_mode,
            domains=domains,
            header_count=header_count,
            interpolate_nulls=interpolate_nulls,
            legend_position=legend_position,
            line_smoothing=line_smoothing,
            series=series,
            stacked_type=stacked_type,
            three_dimensional=three_dimensional,
            total_data_label=total_data_label,
        )


        basic_chart_spec.additional_properties = d
        return basic_chart_spec

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
