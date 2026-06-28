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
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.text_format import TextFormat
  from ..models.treemap_chart_color_scale import TreemapChartColorScale





T = TypeVar("T", bound="TreemapChartSpec")



@_attrs_define
class TreemapChartSpec:
    """ A Treemap chart.

        Attributes:
            color_data (ChartData | Unset): The data included in a domain or series.
            color_scale (TreemapChartColorScale | Unset): A color scale for a treemap chart.
            header_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            header_color_style (ColorStyle | Unset): A color value.
            hide_tooltips (bool | Unset): True to hide tooltips.
            hinted_levels (int | Unset): The number of additional data levels beyond the labeled levels to be shown on the
                treemap chart. These levels are not interactive and are shown without their labels. Defaults to 0 if not
                specified.
            labels (ChartData | Unset): The data included in a domain or series.
            levels (int | Unset): The number of data levels to show on the treemap chart. These levels are interactive and
                are shown with their labels. Defaults to 2 if not specified.
            max_value (float | Unset): The maximum possible data value. Cells with values greater than this will have the
                same color as cells with this value. If not specified, defaults to the actual maximum value from color_data, or
                the maximum value from size_data if color_data is not specified.
            min_value (float | Unset): The minimum possible data value. Cells with values less than this will have the same
                color as cells with this value. If not specified, defaults to the actual minimum value from color_data, or the
                minimum value from size_data if color_data is not specified.
            parent_labels (ChartData | Unset): The data included in a domain or series.
            size_data (ChartData | Unset): The data included in a domain or series.
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
     """

    color_data: ChartData | Unset = UNSET
    color_scale: TreemapChartColorScale | Unset = UNSET
    header_color: Color | Unset = UNSET
    header_color_style: ColorStyle | Unset = UNSET
    hide_tooltips: bool | Unset = UNSET
    hinted_levels: int | Unset = UNSET
    labels: ChartData | Unset = UNSET
    levels: int | Unset = UNSET
    max_value: float | Unset = UNSET
    min_value: float | Unset = UNSET
    parent_labels: ChartData | Unset = UNSET
    size_data: ChartData | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        from ..models.treemap_chart_color_scale import TreemapChartColorScale
        color_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color_data, Unset):
            color_data = self.color_data.to_dict()

        color_scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color_scale, Unset):
            color_scale = self.color_scale.to_dict()

        header_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_color, Unset):
            header_color = self.header_color.to_dict()

        header_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header_color_style, Unset):
            header_color_style = self.header_color_style.to_dict()

        hide_tooltips = self.hide_tooltips

        hinted_levels = self.hinted_levels

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        levels = self.levels

        max_value = self.max_value

        min_value = self.min_value

        parent_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_labels, Unset):
            parent_labels = self.parent_labels.to_dict()

        size_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_data, Unset):
            size_data = self.size_data.to_dict()

        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color_data is not UNSET:
            field_dict["colorData"] = color_data
        if color_scale is not UNSET:
            field_dict["colorScale"] = color_scale
        if header_color is not UNSET:
            field_dict["headerColor"] = header_color
        if header_color_style is not UNSET:
            field_dict["headerColorStyle"] = header_color_style
        if hide_tooltips is not UNSET:
            field_dict["hideTooltips"] = hide_tooltips
        if hinted_levels is not UNSET:
            field_dict["hintedLevels"] = hinted_levels
        if labels is not UNSET:
            field_dict["labels"] = labels
        if levels is not UNSET:
            field_dict["levels"] = levels
        if max_value is not UNSET:
            field_dict["maxValue"] = max_value
        if min_value is not UNSET:
            field_dict["minValue"] = min_value
        if parent_labels is not UNSET:
            field_dict["parentLabels"] = parent_labels
        if size_data is not UNSET:
            field_dict["sizeData"] = size_data
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        from ..models.treemap_chart_color_scale import TreemapChartColorScale
        d = dict(src_dict)
        _color_data = d.pop("colorData", UNSET)
        color_data: ChartData | Unset
        if isinstance(_color_data,  Unset):
            color_data = UNSET
        else:
            color_data = ChartData.from_dict(_color_data)




        _color_scale = d.pop("colorScale", UNSET)
        color_scale: TreemapChartColorScale | Unset
        if isinstance(_color_scale,  Unset):
            color_scale = UNSET
        else:
            color_scale = TreemapChartColorScale.from_dict(_color_scale)




        _header_color = d.pop("headerColor", UNSET)
        header_color: Color | Unset
        if isinstance(_header_color,  Unset):
            header_color = UNSET
        else:
            header_color = Color.from_dict(_header_color)




        _header_color_style = d.pop("headerColorStyle", UNSET)
        header_color_style: ColorStyle | Unset
        if isinstance(_header_color_style,  Unset):
            header_color_style = UNSET
        else:
            header_color_style = ColorStyle.from_dict(_header_color_style)




        hide_tooltips = d.pop("hideTooltips", UNSET)

        hinted_levels = d.pop("hintedLevels", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: ChartData | Unset
        if isinstance(_labels,  Unset):
            labels = UNSET
        else:
            labels = ChartData.from_dict(_labels)




        levels = d.pop("levels", UNSET)

        max_value = d.pop("maxValue", UNSET)

        min_value = d.pop("minValue", UNSET)

        _parent_labels = d.pop("parentLabels", UNSET)
        parent_labels: ChartData | Unset
        if isinstance(_parent_labels,  Unset):
            parent_labels = UNSET
        else:
            parent_labels = ChartData.from_dict(_parent_labels)




        _size_data = d.pop("sizeData", UNSET)
        size_data: ChartData | Unset
        if isinstance(_size_data,  Unset):
            size_data = UNSET
        else:
            size_data = ChartData.from_dict(_size_data)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        treemap_chart_spec = cls(
            color_data=color_data,
            color_scale=color_scale,
            header_color=header_color,
            header_color_style=header_color_style,
            hide_tooltips=hide_tooltips,
            hinted_levels=hinted_levels,
            labels=labels,
            levels=levels,
            max_value=max_value,
            min_value=min_value,
            parent_labels=parent_labels,
            size_data=size_data,
            text_format=text_format,
        )


        treemap_chart_spec.additional_properties = d
        return treemap_chart_spec

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
