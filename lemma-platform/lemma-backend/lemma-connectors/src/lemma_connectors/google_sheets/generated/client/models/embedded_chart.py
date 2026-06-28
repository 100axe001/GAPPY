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
  from ..models.embedded_object_border import EmbeddedObjectBorder
  from ..models.embedded_object_position import EmbeddedObjectPosition





T = TypeVar("T", bound="EmbeddedChart")



@_attrs_define
class EmbeddedChart:
    """ A chart embedded in a sheet.

        Attributes:
            border (EmbeddedObjectBorder | Unset): A border along an embedded object.
            chart_id (int | Unset): The ID of the chart.
            position (EmbeddedObjectPosition | Unset): The position of an embedded object such as a chart.
            spec (ChartSpec | Unset): The specifications of a chart.
     """

    border: EmbeddedObjectBorder | Unset = UNSET
    chart_id: int | Unset = UNSET
    position: EmbeddedObjectPosition | Unset = UNSET
    spec: ChartSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_spec import ChartSpec
        from ..models.embedded_object_border import EmbeddedObjectBorder
        from ..models.embedded_object_position import EmbeddedObjectPosition
        border: dict[str, Any] | Unset = UNSET
        if not isinstance(self.border, Unset):
            border = self.border.to_dict()

        chart_id = self.chart_id

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if border is not UNSET:
            field_dict["border"] = border
        if chart_id is not UNSET:
            field_dict["chartId"] = chart_id
        if position is not UNSET:
            field_dict["position"] = position
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_spec import ChartSpec
        from ..models.embedded_object_border import EmbeddedObjectBorder
        from ..models.embedded_object_position import EmbeddedObjectPosition
        d = dict(src_dict)
        _border = d.pop("border", UNSET)
        border: EmbeddedObjectBorder | Unset
        if isinstance(_border,  Unset):
            border = UNSET
        else:
            border = EmbeddedObjectBorder.from_dict(_border)




        chart_id = d.pop("chartId", UNSET)

        _position = d.pop("position", UNSET)
        position: EmbeddedObjectPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = EmbeddedObjectPosition.from_dict(_position)




        _spec = d.pop("spec", UNSET)
        spec: ChartSpec | Unset
        if isinstance(_spec,  Unset):
            spec = UNSET
        else:
            spec = ChartSpec.from_dict(_spec)




        embedded_chart = cls(
            border=border,
            chart_id=chart_id,
            position=position,
            spec=spec,
        )


        embedded_chart.additional_properties = d
        return embedded_chart

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
