from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.basic_chart_axis_position import BasicChartAxisPosition
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_axis_view_window_options import ChartAxisViewWindowOptions
  from ..models.text_format import TextFormat
  from ..models.text_position import TextPosition





T = TypeVar("T", bound="BasicChartAxis")



@_attrs_define
class BasicChartAxis:
    """ An axis of the chart. A chart may not have more than one axis per axis position.

        Attributes:
            format_ (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field isn't
                specified.
            position (BasicChartAxisPosition | Unset): The position of this axis.
            title (str | Unset): The title of this axis. If set, this overrides any title inferred from headers of the data.
            title_text_position (TextPosition | Unset): Position settings for text.
            view_window_options (ChartAxisViewWindowOptions | Unset): The options that define a "view window" for a chart
                (such as the visible values in an axis).
     """

    format_: TextFormat | Unset = UNSET
    position: BasicChartAxisPosition | Unset = UNSET
    title: str | Unset = UNSET
    title_text_position: TextPosition | Unset = UNSET
    view_window_options: ChartAxisViewWindowOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_axis_view_window_options import ChartAxisViewWindowOptions
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        format_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        position: str | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.value


        title = self.title

        title_text_position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.title_text_position, Unset):
            title_text_position = self.title_text_position.to_dict()

        view_window_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view_window_options, Unset):
            view_window_options = self.view_window_options.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if position is not UNSET:
            field_dict["position"] = position
        if title is not UNSET:
            field_dict["title"] = title
        if title_text_position is not UNSET:
            field_dict["titleTextPosition"] = title_text_position
        if view_window_options is not UNSET:
            field_dict["viewWindowOptions"] = view_window_options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_axis_view_window_options import ChartAxisViewWindowOptions
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        d = dict(src_dict)
        _format_ = d.pop("format", UNSET)
        format_: TextFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = TextFormat.from_dict(_format_)




        _position = d.pop("position", UNSET)
        position: BasicChartAxisPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = BasicChartAxisPosition(_position)




        title = d.pop("title", UNSET)

        _title_text_position = d.pop("titleTextPosition", UNSET)
        title_text_position: TextPosition | Unset
        if isinstance(_title_text_position,  Unset):
            title_text_position = UNSET
        else:
            title_text_position = TextPosition.from_dict(_title_text_position)




        _view_window_options = d.pop("viewWindowOptions", UNSET)
        view_window_options: ChartAxisViewWindowOptions | Unset
        if isinstance(_view_window_options,  Unset):
            view_window_options = UNSET
        else:
            view_window_options = ChartAxisViewWindowOptions.from_dict(_view_window_options)




        basic_chart_axis = cls(
            format_=format_,
            position=position,
            title=title,
            title_text_position=title_text_position,
            view_window_options=view_window_options,
        )


        basic_chart_axis.additional_properties = d
        return basic_chart_axis

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
