from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.basic_chart_series_target_axis import BasicChartSeriesTargetAxis
from ..models.basic_chart_series_type import BasicChartSeriesType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.basic_series_data_point_style_override import BasicSeriesDataPointStyleOverride
  from ..models.chart_data import ChartData
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.data_label import DataLabel
  from ..models.line_style import LineStyle
  from ..models.point_style import PointStyle





T = TypeVar("T", bound="BasicChartSeries")



@_attrs_define
class BasicChartSeries:
    """ A single series of data in a chart. For example, if charting stock prices over time, multiple series may exist, one
    for the "Open Price", "High Price", "Low Price" and "Close Price".

        Attributes:
            color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
                simplicity of conversion to/from color representations in various languages over compactness. For example, the
                fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can
                also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little
                work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't carry
                information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB,
                DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color equality needs
                to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green,
                blue, and alpha values each differ by at most 1e-5. Example (Java): import com.google.type.Color; // ... public
                static java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha() ?
                protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(), protocolor.getGreen(),
                protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float red = (float)
                color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue(); float denominator
                = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator) .setGreen(green /
                denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) { result.setAlpha(
                FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return resultBuilder.build(); }
                // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) { float red = [protocolor
                red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue* alpha_wrapper = [protocolor
                alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor
                colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor* color) { CGFloat red,
                green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) { return nil; } Color* result
                = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result setBlue:blue]; if (alpha <=
                0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; } // ...
                Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac = rgb_color.red || 0.0; var
                greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255);
                var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if (!('alpha' in rgb_color)) {
                return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red,
                green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); }; var rgbToCssColor =
                function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue); var hexString =
                rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for (var i = 0; i <
                missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return resultBuilder.join(''); };
                // ...
            color_style (ColorStyle | Unset): A color value.
            data_label (DataLabel | Unset): Settings for one set of data labels. Data labels are annotations that appear
                next to a set of data, such as the points on a line chart, and provide additional information about what the
                data represents, such as a text representation of the value behind that point on the graph.
            line_style (LineStyle | Unset): Properties that describe the style of a line.
            point_style (PointStyle | Unset): The style of a point on the chart.
            series (ChartData | Unset): The data included in a domain or series.
            style_overrides (list[BasicSeriesDataPointStyleOverride] | Unset): Style override settings for series data
                points.
            target_axis (BasicChartSeriesTargetAxis | Unset): The minor axis that will specify the range of values for this
                series. For example, if charting stocks over time, the "Volume" series may want to be pinned to the right with
                the prices pinned to the left, because the scale of trading volume is different than the scale of prices. It is
                an error to specify an axis that isn't a valid minor axis for the chart's type.
            type_ (BasicChartSeriesType | Unset): The type of this series. Valid only if the chartType is COMBO. Different
                types will change the way the series is visualized. Only LINE, AREA, and COLUMN are supported.
     """

    color: Color | Unset = UNSET
    color_style: ColorStyle | Unset = UNSET
    data_label: DataLabel | Unset = UNSET
    line_style: LineStyle | Unset = UNSET
    point_style: PointStyle | Unset = UNSET
    series: ChartData | Unset = UNSET
    style_overrides: list[BasicSeriesDataPointStyleOverride] | Unset = UNSET
    target_axis: BasicChartSeriesTargetAxis | Unset = UNSET
    type_: BasicChartSeriesType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.basic_series_data_point_style_override import BasicSeriesDataPointStyleOverride
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_label import DataLabel
        from ..models.line_style import LineStyle
        from ..models.point_style import PointStyle
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color_style, Unset):
            color_style = self.color_style.to_dict()

        data_label: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_label, Unset):
            data_label = self.data_label.to_dict()

        line_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.line_style, Unset):
            line_style = self.line_style.to_dict()

        point_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.point_style, Unset):
            point_style = self.point_style.to_dict()

        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        style_overrides: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.style_overrides, Unset):
            style_overrides = []
            for style_overrides_item_data in self.style_overrides:
                style_overrides_item = style_overrides_item_data.to_dict()
                style_overrides.append(style_overrides_item)



        target_axis: str | Unset = UNSET
        if not isinstance(self.target_axis, Unset):
            target_axis = self.target_axis.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if color_style is not UNSET:
            field_dict["colorStyle"] = color_style
        if data_label is not UNSET:
            field_dict["dataLabel"] = data_label
        if line_style is not UNSET:
            field_dict["lineStyle"] = line_style
        if point_style is not UNSET:
            field_dict["pointStyle"] = point_style
        if series is not UNSET:
            field_dict["series"] = series
        if style_overrides is not UNSET:
            field_dict["styleOverrides"] = style_overrides
        if target_axis is not UNSET:
            field_dict["targetAxis"] = target_axis
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.basic_series_data_point_style_override import BasicSeriesDataPointStyleOverride
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.data_label import DataLabel
        from ..models.line_style import LineStyle
        from ..models.point_style import PointStyle
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: Color | Unset
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = Color.from_dict(_color)




        _color_style = d.pop("colorStyle", UNSET)
        color_style: ColorStyle | Unset
        if isinstance(_color_style,  Unset):
            color_style = UNSET
        else:
            color_style = ColorStyle.from_dict(_color_style)




        _data_label = d.pop("dataLabel", UNSET)
        data_label: DataLabel | Unset
        if isinstance(_data_label,  Unset):
            data_label = UNSET
        else:
            data_label = DataLabel.from_dict(_data_label)




        _line_style = d.pop("lineStyle", UNSET)
        line_style: LineStyle | Unset
        if isinstance(_line_style,  Unset):
            line_style = UNSET
        else:
            line_style = LineStyle.from_dict(_line_style)




        _point_style = d.pop("pointStyle", UNSET)
        point_style: PointStyle | Unset
        if isinstance(_point_style,  Unset):
            point_style = UNSET
        else:
            point_style = PointStyle.from_dict(_point_style)




        _series = d.pop("series", UNSET)
        series: ChartData | Unset
        if isinstance(_series,  Unset):
            series = UNSET
        else:
            series = ChartData.from_dict(_series)




        _style_overrides = d.pop("styleOverrides", UNSET)
        style_overrides: list[BasicSeriesDataPointStyleOverride] | Unset = UNSET
        if _style_overrides is not UNSET:
            style_overrides = []
            for style_overrides_item_data in _style_overrides:
                style_overrides_item = BasicSeriesDataPointStyleOverride.from_dict(style_overrides_item_data)



                style_overrides.append(style_overrides_item)


        _target_axis = d.pop("targetAxis", UNSET)
        target_axis: BasicChartSeriesTargetAxis | Unset
        if isinstance(_target_axis,  Unset):
            target_axis = UNSET
        else:
            target_axis = BasicChartSeriesTargetAxis(_target_axis)




        _type_ = d.pop("type", UNSET)
        type_: BasicChartSeriesType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = BasicChartSeriesType(_type_)




        basic_chart_series = cls(
            color=color,
            color_style=color_style,
            data_label=data_label,
            line_style=line_style,
            point_style=point_style,
            series=series,
            style_overrides=style_overrides,
            target_axis=target_axis,
            type_=type_,
        )


        basic_chart_series.additional_properties = d
        return basic_chart_series

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
