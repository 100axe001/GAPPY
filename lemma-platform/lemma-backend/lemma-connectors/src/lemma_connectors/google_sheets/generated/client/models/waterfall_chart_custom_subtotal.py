from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WaterfallChartCustomSubtotal")



@_attrs_define
class WaterfallChartCustomSubtotal:
    """ A custom subtotal column for a waterfall chart series.

        Attributes:
            data_is_subtotal (bool | Unset): True if the data point at subtotal_index is the subtotal. If false, the
                subtotal will be computed and appear after the data point.
            label (str | Unset): A label for the subtotal column.
            subtotal_index (int | Unset): The 0-based index of a data point within the series. If data_is_subtotal is true,
                the data point at this index is the subtotal. Otherwise, the subtotal appears after the data point with this
                index. A series can have multiple subtotals at arbitrary indices, but subtotals do not affect the indices of the
                data points. For example, if a series has three data points, their indices will always be 0, 1, and 2,
                regardless of how many subtotals exist on the series or what data points they are associated with.
     """

    data_is_subtotal: bool | Unset = UNSET
    label: str | Unset = UNSET
    subtotal_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_is_subtotal = self.data_is_subtotal

        label = self.label

        subtotal_index = self.subtotal_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_is_subtotal is not UNSET:
            field_dict["dataIsSubtotal"] = data_is_subtotal
        if label is not UNSET:
            field_dict["label"] = label
        if subtotal_index is not UNSET:
            field_dict["subtotalIndex"] = subtotal_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_is_subtotal = d.pop("dataIsSubtotal", UNSET)

        label = d.pop("label", UNSET)

        subtotal_index = d.pop("subtotalIndex", UNSET)

        waterfall_chart_custom_subtotal = cls(
            data_is_subtotal=data_is_subtotal,
            label=label,
            subtotal_index=subtotal_index,
        )


        waterfall_chart_custom_subtotal.additional_properties = d
        return waterfall_chart_custom_subtotal

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
