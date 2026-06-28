from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.waterfall_chart_spec_stacked_type import WaterfallChartSpecStackedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_label import DataLabel
  from ..models.line_style import LineStyle
  from ..models.waterfall_chart_domain import WaterfallChartDomain
  from ..models.waterfall_chart_series import WaterfallChartSeries





T = TypeVar("T", bound="WaterfallChartSpec")



@_attrs_define
class WaterfallChartSpec:
    """ A waterfall chart.

        Attributes:
            connector_line_style (LineStyle | Unset): Properties that describe the style of a line.
            domain (WaterfallChartDomain | Unset): The domain of a waterfall chart.
            first_value_is_total (bool | Unset): True to interpret the first value as a total.
            hide_connector_lines (bool | Unset): True to hide connector lines between columns.
            series (list[WaterfallChartSeries] | Unset): The data this waterfall chart is visualizing.
            stacked_type (WaterfallChartSpecStackedType | Unset): The stacked type.
            total_data_label (DataLabel | Unset): Settings for one set of data labels. Data labels are annotations that
                appear next to a set of data, such as the points on a line chart, and provide additional information about what
                the data represents, such as a text representation of the value behind that point on the graph.
     """

    connector_line_style: LineStyle | Unset = UNSET
    domain: WaterfallChartDomain | Unset = UNSET
    first_value_is_total: bool | Unset = UNSET
    hide_connector_lines: bool | Unset = UNSET
    series: list[WaterfallChartSeries] | Unset = UNSET
    stacked_type: WaterfallChartSpecStackedType | Unset = UNSET
    total_data_label: DataLabel | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_label import DataLabel
        from ..models.line_style import LineStyle
        from ..models.waterfall_chart_domain import WaterfallChartDomain
        from ..models.waterfall_chart_series import WaterfallChartSeries
        connector_line_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connector_line_style, Unset):
            connector_line_style = self.connector_line_style.to_dict()

        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        first_value_is_total = self.first_value_is_total

        hide_connector_lines = self.hide_connector_lines

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)



        stacked_type: str | Unset = UNSET
        if not isinstance(self.stacked_type, Unset):
            stacked_type = self.stacked_type.value


        total_data_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_data_label, Unset):
            total_data_label = self.total_data_label.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connector_line_style is not UNSET:
            field_dict["connectorLineStyle"] = connector_line_style
        if domain is not UNSET:
            field_dict["domain"] = domain
        if first_value_is_total is not UNSET:
            field_dict["firstValueIsTotal"] = first_value_is_total
        if hide_connector_lines is not UNSET:
            field_dict["hideConnectorLines"] = hide_connector_lines
        if series is not UNSET:
            field_dict["series"] = series
        if stacked_type is not UNSET:
            field_dict["stackedType"] = stacked_type
        if total_data_label is not UNSET:
            field_dict["totalDataLabel"] = total_data_label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_label import DataLabel
        from ..models.line_style import LineStyle
        from ..models.waterfall_chart_domain import WaterfallChartDomain
        from ..models.waterfall_chart_series import WaterfallChartSeries
        d = dict(src_dict)
        _connector_line_style = d.pop("connectorLineStyle", UNSET)
        connector_line_style: LineStyle | Unset
        if isinstance(_connector_line_style,  Unset):
            connector_line_style = UNSET
        else:
            connector_line_style = LineStyle.from_dict(_connector_line_style)




        _domain = d.pop("domain", UNSET)
        domain: WaterfallChartDomain | Unset
        if isinstance(_domain,  Unset):
            domain = UNSET
        else:
            domain = WaterfallChartDomain.from_dict(_domain)




        first_value_is_total = d.pop("firstValueIsTotal", UNSET)

        hide_connector_lines = d.pop("hideConnectorLines", UNSET)

        _series = d.pop("series", UNSET)
        series: list[WaterfallChartSeries] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = WaterfallChartSeries.from_dict(series_item_data)



                series.append(series_item)


        _stacked_type = d.pop("stackedType", UNSET)
        stacked_type: WaterfallChartSpecStackedType | Unset
        if isinstance(_stacked_type,  Unset):
            stacked_type = UNSET
        else:
            stacked_type = WaterfallChartSpecStackedType(_stacked_type)




        _total_data_label = d.pop("totalDataLabel", UNSET)
        total_data_label: DataLabel | Unset
        if isinstance(_total_data_label,  Unset):
            total_data_label = UNSET
        else:
            total_data_label = DataLabel.from_dict(_total_data_label)




        waterfall_chart_spec = cls(
            connector_line_style=connector_line_style,
            domain=domain,
            first_value_is_total=first_value_is_total,
            hide_connector_lines=hide_connector_lines,
            series=series,
            stacked_type=stacked_type,
            total_data_label=total_data_label,
        )


        waterfall_chart_spec.additional_properties = d
        return waterfall_chart_spec

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
