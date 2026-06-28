from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.org_chart_spec_node_size import OrgChartSpecNodeSize
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData
  from ..models.color import Color
  from ..models.color_style import ColorStyle





T = TypeVar("T", bound="OrgChartSpec")



@_attrs_define
class OrgChartSpec:
    """ An org chart. Org charts require a unique set of labels in labels and may optionally include parent_labels and
    tooltips. parent_labels contain, for each node, the label identifying the parent node. tooltips contain, for each
    node, an optional tooltip. For example, to describe an OrgChart with Alice as the CEO, Bob as the President
    (reporting to Alice) and Cathy as VP of Sales (also reporting to Alice), have labels contain "Alice", "Bob",
    "Cathy", parent_labels contain "", "Alice", "Alice" and tooltips contain "CEO", "President", "VP Sales".

        Attributes:
            labels (ChartData | Unset): The data included in a domain or series.
            node_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            node_color_style (ColorStyle | Unset): A color value.
            node_size (OrgChartSpecNodeSize | Unset): The size of the org chart nodes.
            parent_labels (ChartData | Unset): The data included in a domain or series.
            selected_node_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed
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
            selected_node_color_style (ColorStyle | Unset): A color value.
            tooltips (ChartData | Unset): The data included in a domain or series.
     """

    labels: ChartData | Unset = UNSET
    node_color: Color | Unset = UNSET
    node_color_style: ColorStyle | Unset = UNSET
    node_size: OrgChartSpecNodeSize | Unset = UNSET
    parent_labels: ChartData | Unset = UNSET
    selected_node_color: Color | Unset = UNSET
    selected_node_color_style: ColorStyle | Unset = UNSET
    tooltips: ChartData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        node_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_color, Unset):
            node_color = self.node_color.to_dict()

        node_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_color_style, Unset):
            node_color_style = self.node_color_style.to_dict()

        node_size: str | Unset = UNSET
        if not isinstance(self.node_size, Unset):
            node_size = self.node_size.value


        parent_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_labels, Unset):
            parent_labels = self.parent_labels.to_dict()

        selected_node_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_node_color, Unset):
            selected_node_color = self.selected_node_color.to_dict()

        selected_node_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_node_color_style, Unset):
            selected_node_color_style = self.selected_node_color_style.to_dict()

        tooltips: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tooltips, Unset):
            tooltips = self.tooltips.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if labels is not UNSET:
            field_dict["labels"] = labels
        if node_color is not UNSET:
            field_dict["nodeColor"] = node_color
        if node_color_style is not UNSET:
            field_dict["nodeColorStyle"] = node_color_style
        if node_size is not UNSET:
            field_dict["nodeSize"] = node_size
        if parent_labels is not UNSET:
            field_dict["parentLabels"] = parent_labels
        if selected_node_color is not UNSET:
            field_dict["selectedNodeColor"] = selected_node_color
        if selected_node_color_style is not UNSET:
            field_dict["selectedNodeColorStyle"] = selected_node_color_style
        if tooltips is not UNSET:
            field_dict["tooltips"] = tooltips

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: ChartData | Unset
        if isinstance(_labels,  Unset):
            labels = UNSET
        else:
            labels = ChartData.from_dict(_labels)




        _node_color = d.pop("nodeColor", UNSET)
        node_color: Color | Unset
        if isinstance(_node_color,  Unset):
            node_color = UNSET
        else:
            node_color = Color.from_dict(_node_color)




        _node_color_style = d.pop("nodeColorStyle", UNSET)
        node_color_style: ColorStyle | Unset
        if isinstance(_node_color_style,  Unset):
            node_color_style = UNSET
        else:
            node_color_style = ColorStyle.from_dict(_node_color_style)




        _node_size = d.pop("nodeSize", UNSET)
        node_size: OrgChartSpecNodeSize | Unset
        if isinstance(_node_size,  Unset):
            node_size = UNSET
        else:
            node_size = OrgChartSpecNodeSize(_node_size)




        _parent_labels = d.pop("parentLabels", UNSET)
        parent_labels: ChartData | Unset
        if isinstance(_parent_labels,  Unset):
            parent_labels = UNSET
        else:
            parent_labels = ChartData.from_dict(_parent_labels)




        _selected_node_color = d.pop("selectedNodeColor", UNSET)
        selected_node_color: Color | Unset
        if isinstance(_selected_node_color,  Unset):
            selected_node_color = UNSET
        else:
            selected_node_color = Color.from_dict(_selected_node_color)




        _selected_node_color_style = d.pop("selectedNodeColorStyle", UNSET)
        selected_node_color_style: ColorStyle | Unset
        if isinstance(_selected_node_color_style,  Unset):
            selected_node_color_style = UNSET
        else:
            selected_node_color_style = ColorStyle.from_dict(_selected_node_color_style)




        _tooltips = d.pop("tooltips", UNSET)
        tooltips: ChartData | Unset
        if isinstance(_tooltips,  Unset):
            tooltips = UNSET
        else:
            tooltips = ChartData.from_dict(_tooltips)




        org_chart_spec = cls(
            labels=labels,
            node_color=node_color,
            node_color_style=node_color_style,
            node_size=node_size,
            parent_labels=parent_labels,
            selected_node_color=selected_node_color,
            selected_node_color_style=selected_node_color_style,
            tooltips=tooltips,
        )


        org_chart_spec.additional_properties = d
        return org_chart_spec

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
