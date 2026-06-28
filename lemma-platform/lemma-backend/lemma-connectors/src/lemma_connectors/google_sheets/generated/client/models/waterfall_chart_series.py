from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData
  from ..models.data_label import DataLabel
  from ..models.waterfall_chart_column_style import WaterfallChartColumnStyle
  from ..models.waterfall_chart_custom_subtotal import WaterfallChartCustomSubtotal





T = TypeVar("T", bound="WaterfallChartSeries")



@_attrs_define
class WaterfallChartSeries:
    """ A single series of data for a waterfall chart.

        Attributes:
            custom_subtotals (list[WaterfallChartCustomSubtotal] | Unset): Custom subtotal columns appearing in this series.
                The order in which subtotals are defined is not significant. Only one subtotal may be defined for each data
                point.
            data (ChartData | Unset): The data included in a domain or series.
            data_label (DataLabel | Unset): Settings for one set of data labels. Data labels are annotations that appear
                next to a set of data, such as the points on a line chart, and provide additional information about what the
                data represents, such as a text representation of the value behind that point on the graph.
            hide_trailing_subtotal (bool | Unset): True to hide the subtotal column from the end of the series. By default,
                a subtotal column will appear at the end of each series. Setting this field to true will hide that subtotal
                column for this series.
            negative_columns_style (WaterfallChartColumnStyle | Unset): Styles for a waterfall chart column.
            positive_columns_style (WaterfallChartColumnStyle | Unset): Styles for a waterfall chart column.
            subtotal_columns_style (WaterfallChartColumnStyle | Unset): Styles for a waterfall chart column.
     """

    custom_subtotals: list[WaterfallChartCustomSubtotal] | Unset = UNSET
    data: ChartData | Unset = UNSET
    data_label: DataLabel | Unset = UNSET
    hide_trailing_subtotal: bool | Unset = UNSET
    negative_columns_style: WaterfallChartColumnStyle | Unset = UNSET
    positive_columns_style: WaterfallChartColumnStyle | Unset = UNSET
    subtotal_columns_style: WaterfallChartColumnStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        from ..models.data_label import DataLabel
        from ..models.waterfall_chart_column_style import WaterfallChartColumnStyle
        from ..models.waterfall_chart_custom_subtotal import WaterfallChartCustomSubtotal
        custom_subtotals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_subtotals, Unset):
            custom_subtotals = []
            for custom_subtotals_item_data in self.custom_subtotals:
                custom_subtotals_item = custom_subtotals_item_data.to_dict()
                custom_subtotals.append(custom_subtotals_item)



        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        data_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_label, Unset):
            data_label = self.data_label.to_dict()

        hide_trailing_subtotal = self.hide_trailing_subtotal

        negative_columns_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.negative_columns_style, Unset):
            negative_columns_style = self.negative_columns_style.to_dict()

        positive_columns_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positive_columns_style, Unset):
            positive_columns_style = self.positive_columns_style.to_dict()

        subtotal_columns_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subtotal_columns_style, Unset):
            subtotal_columns_style = self.subtotal_columns_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_subtotals is not UNSET:
            field_dict["customSubtotals"] = custom_subtotals
        if data is not UNSET:
            field_dict["data"] = data
        if data_label is not UNSET:
            field_dict["dataLabel"] = data_label
        if hide_trailing_subtotal is not UNSET:
            field_dict["hideTrailingSubtotal"] = hide_trailing_subtotal
        if negative_columns_style is not UNSET:
            field_dict["negativeColumnsStyle"] = negative_columns_style
        if positive_columns_style is not UNSET:
            field_dict["positiveColumnsStyle"] = positive_columns_style
        if subtotal_columns_style is not UNSET:
            field_dict["subtotalColumnsStyle"] = subtotal_columns_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        from ..models.data_label import DataLabel
        from ..models.waterfall_chart_column_style import WaterfallChartColumnStyle
        from ..models.waterfall_chart_custom_subtotal import WaterfallChartCustomSubtotal
        d = dict(src_dict)
        _custom_subtotals = d.pop("customSubtotals", UNSET)
        custom_subtotals: list[WaterfallChartCustomSubtotal] | Unset = UNSET
        if _custom_subtotals is not UNSET:
            custom_subtotals = []
            for custom_subtotals_item_data in _custom_subtotals:
                custom_subtotals_item = WaterfallChartCustomSubtotal.from_dict(custom_subtotals_item_data)



                custom_subtotals.append(custom_subtotals_item)


        _data = d.pop("data", UNSET)
        data: ChartData | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = ChartData.from_dict(_data)




        _data_label = d.pop("dataLabel", UNSET)
        data_label: DataLabel | Unset
        if isinstance(_data_label,  Unset):
            data_label = UNSET
        else:
            data_label = DataLabel.from_dict(_data_label)




        hide_trailing_subtotal = d.pop("hideTrailingSubtotal", UNSET)

        _negative_columns_style = d.pop("negativeColumnsStyle", UNSET)
        negative_columns_style: WaterfallChartColumnStyle | Unset
        if isinstance(_negative_columns_style,  Unset):
            negative_columns_style = UNSET
        else:
            negative_columns_style = WaterfallChartColumnStyle.from_dict(_negative_columns_style)




        _positive_columns_style = d.pop("positiveColumnsStyle", UNSET)
        positive_columns_style: WaterfallChartColumnStyle | Unset
        if isinstance(_positive_columns_style,  Unset):
            positive_columns_style = UNSET
        else:
            positive_columns_style = WaterfallChartColumnStyle.from_dict(_positive_columns_style)




        _subtotal_columns_style = d.pop("subtotalColumnsStyle", UNSET)
        subtotal_columns_style: WaterfallChartColumnStyle | Unset
        if isinstance(_subtotal_columns_style,  Unset):
            subtotal_columns_style = UNSET
        else:
            subtotal_columns_style = WaterfallChartColumnStyle.from_dict(_subtotal_columns_style)




        waterfall_chart_series = cls(
            custom_subtotals=custom_subtotals,
            data=data,
            data_label=data_label,
            hide_trailing_subtotal=hide_trailing_subtotal,
            negative_columns_style=negative_columns_style,
            positive_columns_style=positive_columns_style,
            subtotal_columns_style=subtotal_columns_style,
        )


        waterfall_chart_series.additional_properties = d
        return waterfall_chart_series

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
