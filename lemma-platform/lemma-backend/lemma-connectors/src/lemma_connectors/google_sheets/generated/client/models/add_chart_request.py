from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_chart import EmbeddedChart





T = TypeVar("T", bound="AddChartRequest")



@_attrs_define
class AddChartRequest:
    """ Adds a chart to a sheet in the spreadsheet.

        Attributes:
            chart (EmbeddedChart | Unset): A chart embedded in a sheet.
     """

    chart: EmbeddedChart | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_chart import EmbeddedChart
        chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chart, Unset):
            chart = self.chart.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chart is not UNSET:
            field_dict["chart"] = chart

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_chart import EmbeddedChart
        d = dict(src_dict)
        _chart = d.pop("chart", UNSET)
        chart: EmbeddedChart | Unset
        if isinstance(_chart,  Unset):
            chart = UNSET
        else:
            chart = EmbeddedChart.from_dict(_chart)




        add_chart_request = cls(
            chart=chart,
        )


        add_chart_request.additional_properties = d
        return add_chart_request

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
