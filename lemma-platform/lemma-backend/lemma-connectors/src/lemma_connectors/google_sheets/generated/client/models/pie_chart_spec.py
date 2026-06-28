from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pie_chart_spec_legend_position import PieChartSpecLegendPosition
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData





T = TypeVar("T", bound="PieChartSpec")



@_attrs_define
class PieChartSpec:
    """ A pie chart.

        Attributes:
            domain (ChartData | Unset): The data included in a domain or series.
            legend_position (PieChartSpecLegendPosition | Unset): Where the legend of the pie chart should be drawn.
            pie_hole (float | Unset): The size of the hole in the pie chart.
            series (ChartData | Unset): The data included in a domain or series.
            three_dimensional (bool | Unset): True if the pie is three dimensional.
     """

    domain: ChartData | Unset = UNSET
    legend_position: PieChartSpecLegendPosition | Unset = UNSET
    pie_hole: float | Unset = UNSET
    series: ChartData | Unset = UNSET
    three_dimensional: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        legend_position: str | Unset = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value


        pie_hole = self.pie_hole

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        three_dimensional = self.three_dimensional


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if domain is not UNSET:
            field_dict["domain"] = domain
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if pie_hole is not UNSET:
            field_dict["pieHole"] = pie_hole
        if series is not UNSET:
            field_dict["series"] = series
        if three_dimensional is not UNSET:
            field_dict["threeDimensional"] = three_dimensional

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        d = dict(src_dict)
        _domain = d.pop("domain", UNSET)
        domain: ChartData | Unset
        if isinstance(_domain,  Unset):
            domain = UNSET
        else:
            domain = ChartData.from_dict(_domain)




        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: PieChartSpecLegendPosition | Unset
        if isinstance(_legend_position,  Unset):
            legend_position = UNSET
        else:
            legend_position = PieChartSpecLegendPosition(_legend_position)




        pie_hole = d.pop("pieHole", UNSET)

        _series = d.pop("series", UNSET)
        series: ChartData | Unset
        if isinstance(_series,  Unset):
            series = UNSET
        else:
            series = ChartData.from_dict(_series)




        three_dimensional = d.pop("threeDimensional", UNSET)

        pie_chart_spec = cls(
            domain=domain,
            legend_position=legend_position,
            pie_hole=pie_hole,
            series=series,
            three_dimensional=three_dimensional,
        )


        pie_chart_spec.additional_properties = d
        return pie_chart_spec

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
