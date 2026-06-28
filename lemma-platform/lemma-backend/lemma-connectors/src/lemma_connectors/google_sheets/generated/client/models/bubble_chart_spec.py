from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.bubble_chart_spec_legend_position import BubbleChartSpecLegendPosition
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.text_format import TextFormat





T = TypeVar("T", bound="BubbleChartSpec")



@_attrs_define
class BubbleChartSpec:
    """ A bubble chart.

        Attributes:
            bubble_border_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
                for simplicity of conversion to/from color representations in various languages over compactness. For example,
                the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it
                can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a
                little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't
                carry information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB,
                Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color
                equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all
                their red, green, blue, and alpha values each differ by at most 1e-5. Example (Java): import
                com.google.type.Color; // ... public static java.awt.Color fromProto(Color protocolor) { float alpha =
                protocolor.hasAlpha() ? protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(),
                protocolor.getGreen(), protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float
                red = (float) color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue();
                float denominator = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator)
                .setGreen(green / denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) {
                result.setAlpha( FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return
                resultBuilder.build(); } // ... Example (iOS / Obj-C): // ... static UIColor* fromProto(Color* protocolor) {
                float red = [protocolor red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue*
                alpha_wrapper = [protocolor alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper
                value]; } return [UIColor colorWithRed:red green:green blue:blue alpha:alpha]; } static Color* toProto(UIColor*
                color) { CGFloat red, green, blue, alpha; if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
                return nil; } Color* result = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result
                setBlue:blue]; if (alpha <= 0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease];
                return result; } // ... Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac =
                rgb_color.red || 0.0; var greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red =
                Math.floor(redFrac * 255); var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if
                (!('alpha' in rgb_color)) { return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value ||
                0.0; var rgbParams = [red, green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); };
                var rgbToCssColor = function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue);
                var hexString = rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for
                (var i = 0; i < missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return
                resultBuilder.join(''); }; // ...
            bubble_border_color_style (ColorStyle | Unset): A color value.
            bubble_labels (ChartData | Unset): The data included in a domain or series.
            bubble_max_radius_size (int | Unset): The max radius size of the bubbles, in pixels. If specified, the field
                must be a positive value.
            bubble_min_radius_size (int | Unset): The minimum radius size of the bubbles, in pixels. If specific, the field
                must be a positive value.
            bubble_opacity (float | Unset): The opacity of the bubbles between 0 and 1.0. 0 is fully transparent and 1 is
                fully opaque.
            bubble_sizes (ChartData | Unset): The data included in a domain or series.
            bubble_text_style (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the
                field isn't specified.
            domain (ChartData | Unset): The data included in a domain or series.
            group_ids (ChartData | Unset): The data included in a domain or series.
            legend_position (BubbleChartSpecLegendPosition | Unset): Where the legend of the chart should be drawn.
            series (ChartData | Unset): The data included in a domain or series.
     """

    bubble_border_color: Color | Unset = UNSET
    bubble_border_color_style: ColorStyle | Unset = UNSET
    bubble_labels: ChartData | Unset = UNSET
    bubble_max_radius_size: int | Unset = UNSET
    bubble_min_radius_size: int | Unset = UNSET
    bubble_opacity: float | Unset = UNSET
    bubble_sizes: ChartData | Unset = UNSET
    bubble_text_style: TextFormat | Unset = UNSET
    domain: ChartData | Unset = UNSET
    group_ids: ChartData | Unset = UNSET
    legend_position: BubbleChartSpecLegendPosition | Unset = UNSET
    series: ChartData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        bubble_border_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_border_color, Unset):
            bubble_border_color = self.bubble_border_color.to_dict()

        bubble_border_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_border_color_style, Unset):
            bubble_border_color_style = self.bubble_border_color_style.to_dict()

        bubble_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_labels, Unset):
            bubble_labels = self.bubble_labels.to_dict()

        bubble_max_radius_size = self.bubble_max_radius_size

        bubble_min_radius_size = self.bubble_min_radius_size

        bubble_opacity = self.bubble_opacity

        bubble_sizes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_sizes, Unset):
            bubble_sizes = self.bubble_sizes.to_dict()

        bubble_text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bubble_text_style, Unset):
            bubble_text_style = self.bubble_text_style.to_dict()

        domain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain, Unset):
            domain = self.domain.to_dict()

        group_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids.to_dict()

        legend_position: str | Unset = UNSET
        if not isinstance(self.legend_position, Unset):
            legend_position = self.legend_position.value


        series: dict[str, Any] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bubble_border_color is not UNSET:
            field_dict["bubbleBorderColor"] = bubble_border_color
        if bubble_border_color_style is not UNSET:
            field_dict["bubbleBorderColorStyle"] = bubble_border_color_style
        if bubble_labels is not UNSET:
            field_dict["bubbleLabels"] = bubble_labels
        if bubble_max_radius_size is not UNSET:
            field_dict["bubbleMaxRadiusSize"] = bubble_max_radius_size
        if bubble_min_radius_size is not UNSET:
            field_dict["bubbleMinRadiusSize"] = bubble_min_radius_size
        if bubble_opacity is not UNSET:
            field_dict["bubbleOpacity"] = bubble_opacity
        if bubble_sizes is not UNSET:
            field_dict["bubbleSizes"] = bubble_sizes
        if bubble_text_style is not UNSET:
            field_dict["bubbleTextStyle"] = bubble_text_style
        if domain is not UNSET:
            field_dict["domain"] = domain
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if legend_position is not UNSET:
            field_dict["legendPosition"] = legend_position
        if series is not UNSET:
            field_dict["series"] = series

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        d = dict(src_dict)
        _bubble_border_color = d.pop("bubbleBorderColor", UNSET)
        bubble_border_color: Color | Unset
        if isinstance(_bubble_border_color,  Unset):
            bubble_border_color = UNSET
        else:
            bubble_border_color = Color.from_dict(_bubble_border_color)




        _bubble_border_color_style = d.pop("bubbleBorderColorStyle", UNSET)
        bubble_border_color_style: ColorStyle | Unset
        if isinstance(_bubble_border_color_style,  Unset):
            bubble_border_color_style = UNSET
        else:
            bubble_border_color_style = ColorStyle.from_dict(_bubble_border_color_style)




        _bubble_labels = d.pop("bubbleLabels", UNSET)
        bubble_labels: ChartData | Unset
        if isinstance(_bubble_labels,  Unset):
            bubble_labels = UNSET
        else:
            bubble_labels = ChartData.from_dict(_bubble_labels)




        bubble_max_radius_size = d.pop("bubbleMaxRadiusSize", UNSET)

        bubble_min_radius_size = d.pop("bubbleMinRadiusSize", UNSET)

        bubble_opacity = d.pop("bubbleOpacity", UNSET)

        _bubble_sizes = d.pop("bubbleSizes", UNSET)
        bubble_sizes: ChartData | Unset
        if isinstance(_bubble_sizes,  Unset):
            bubble_sizes = UNSET
        else:
            bubble_sizes = ChartData.from_dict(_bubble_sizes)




        _bubble_text_style = d.pop("bubbleTextStyle", UNSET)
        bubble_text_style: TextFormat | Unset
        if isinstance(_bubble_text_style,  Unset):
            bubble_text_style = UNSET
        else:
            bubble_text_style = TextFormat.from_dict(_bubble_text_style)




        _domain = d.pop("domain", UNSET)
        domain: ChartData | Unset
        if isinstance(_domain,  Unset):
            domain = UNSET
        else:
            domain = ChartData.from_dict(_domain)




        _group_ids = d.pop("groupIds", UNSET)
        group_ids: ChartData | Unset
        if isinstance(_group_ids,  Unset):
            group_ids = UNSET
        else:
            group_ids = ChartData.from_dict(_group_ids)




        _legend_position = d.pop("legendPosition", UNSET)
        legend_position: BubbleChartSpecLegendPosition | Unset
        if isinstance(_legend_position,  Unset):
            legend_position = UNSET
        else:
            legend_position = BubbleChartSpecLegendPosition(_legend_position)




        _series = d.pop("series", UNSET)
        series: ChartData | Unset
        if isinstance(_series,  Unset):
            series = UNSET
        else:
            series = ChartData.from_dict(_series)




        bubble_chart_spec = cls(
            bubble_border_color=bubble_border_color,
            bubble_border_color_style=bubble_border_color_style,
            bubble_labels=bubble_labels,
            bubble_max_radius_size=bubble_max_radius_size,
            bubble_min_radius_size=bubble_min_radius_size,
            bubble_opacity=bubble_opacity,
            bubble_sizes=bubble_sizes,
            bubble_text_style=bubble_text_style,
            domain=domain,
            group_ids=group_ids,
            legend_position=legend_position,
            series=series,
        )


        bubble_chart_spec.additional_properties = d
        return bubble_chart_spec

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
