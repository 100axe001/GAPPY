from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_spec import ChartSpec





T = TypeVar("T", bound="UpdateChartSpecRequest")



@_attrs_define
class UpdateChartSpecRequest:
    """ Updates a chart's specifications. (This does not move or resize a chart. To move or resize a chart, use
    UpdateEmbeddedObjectPositionRequest.)

        Attributes:
            chart_id (int | Unset): The ID of the chart to update.
            spec (ChartSpec | Unset): The specifications of a chart.
     """

    chart_id: int | Unset = UNSET
    spec: ChartSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_spec import ChartSpec
        chart_id = self.chart_id

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chart_id is not UNSET:
            field_dict["chartId"] = chart_id
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_spec import ChartSpec
        d = dict(src_dict)
        chart_id = d.pop("chartId", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: ChartSpec | Unset
        if isinstance(_spec,  Unset):
            spec = UNSET
        else:
            spec = ChartSpec.from_dict(_spec)




        update_chart_spec_request = cls(
            chart_id=chart_id,
            spec=spec,
        )


        update_chart_spec_request.additional_properties = d
        return update_chart_spec_request

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
