from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.chart_axis_view_window_options_view_window_mode import ChartAxisViewWindowOptionsViewWindowMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="ChartAxisViewWindowOptions")



@_attrs_define
class ChartAxisViewWindowOptions:
    """ The options that define a "view window" for a chart (such as the visible values in an axis).

        Attributes:
            view_window_max (float | Unset): The maximum numeric value to be shown in this view window. If unset, will
                automatically determine a maximum value that looks good for the data.
            view_window_min (float | Unset): The minimum numeric value to be shown in this view window. If unset, will
                automatically determine a minimum value that looks good for the data.
            view_window_mode (ChartAxisViewWindowOptionsViewWindowMode | Unset): The view window's mode.
     """

    view_window_max: float | Unset = UNSET
    view_window_min: float | Unset = UNSET
    view_window_mode: ChartAxisViewWindowOptionsViewWindowMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        view_window_max = self.view_window_max

        view_window_min = self.view_window_min

        view_window_mode: str | Unset = UNSET
        if not isinstance(self.view_window_mode, Unset):
            view_window_mode = self.view_window_mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if view_window_max is not UNSET:
            field_dict["viewWindowMax"] = view_window_max
        if view_window_min is not UNSET:
            field_dict["viewWindowMin"] = view_window_min
        if view_window_mode is not UNSET:
            field_dict["viewWindowMode"] = view_window_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        view_window_max = d.pop("viewWindowMax", UNSET)

        view_window_min = d.pop("viewWindowMin", UNSET)

        _view_window_mode = d.pop("viewWindowMode", UNSET)
        view_window_mode: ChartAxisViewWindowOptionsViewWindowMode | Unset
        if isinstance(_view_window_mode,  Unset):
            view_window_mode = UNSET
        else:
            view_window_mode = ChartAxisViewWindowOptionsViewWindowMode(_view_window_mode)




        chart_axis_view_window_options = cls(
            view_window_max=view_window_max,
            view_window_min=view_window_min,
            view_window_mode=view_window_mode,
        )


        chart_axis_view_window_options.additional_properties = d
        return chart_axis_view_window_options

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
