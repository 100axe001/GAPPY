from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.baseline_value_format_comparison_type import BaselineValueFormatComparisonType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle
  from ..models.text_format import TextFormat
  from ..models.text_position import TextPosition





T = TypeVar("T", bound="BaselineValueFormat")



@_attrs_define
class BaselineValueFormat:
    """ Formatting options for baseline value.

        Attributes:
            comparison_type (BaselineValueFormatComparisonType | Unset): The comparison type of key value with baseline
                value.
            description (str | Unset): Description which is appended after the baseline value. This field is optional.
            negative_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            negative_color_style (ColorStyle | Unset): A color value.
            position (TextPosition | Unset): Position settings for text.
            positive_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            positive_color_style (ColorStyle | Unset): A color value.
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
     """

    comparison_type: BaselineValueFormatComparisonType | Unset = UNSET
    description: str | Unset = UNSET
    negative_color: Color | Unset = UNSET
    negative_color_style: ColorStyle | Unset = UNSET
    position: TextPosition | Unset = UNSET
    positive_color: Color | Unset = UNSET
    positive_color_style: ColorStyle | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        comparison_type: str | Unset = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value


        description = self.description

        negative_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.negative_color, Unset):
            negative_color = self.negative_color.to_dict()

        negative_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.negative_color_style, Unset):
            negative_color_style = self.negative_color_style.to_dict()

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        positive_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positive_color, Unset):
            positive_color = self.positive_color.to_dict()

        positive_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.positive_color_style, Unset):
            positive_color_style = self.positive_color_style.to_dict()

        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comparison_type is not UNSET:
            field_dict["comparisonType"] = comparison_type
        if description is not UNSET:
            field_dict["description"] = description
        if negative_color is not UNSET:
            field_dict["negativeColor"] = negative_color
        if negative_color_style is not UNSET:
            field_dict["negativeColorStyle"] = negative_color_style
        if position is not UNSET:
            field_dict["position"] = position
        if positive_color is not UNSET:
            field_dict["positiveColor"] = positive_color
        if positive_color_style is not UNSET:
            field_dict["positiveColorStyle"] = positive_color_style
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        from ..models.text_format import TextFormat
        from ..models.text_position import TextPosition
        d = dict(src_dict)
        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: BaselineValueFormatComparisonType | Unset
        if isinstance(_comparison_type,  Unset):
            comparison_type = UNSET
        else:
            comparison_type = BaselineValueFormatComparisonType(_comparison_type)




        description = d.pop("description", UNSET)

        _negative_color = d.pop("negativeColor", UNSET)
        negative_color: Color | Unset
        if isinstance(_negative_color,  Unset):
            negative_color = UNSET
        else:
            negative_color = Color.from_dict(_negative_color)




        _negative_color_style = d.pop("negativeColorStyle", UNSET)
        negative_color_style: ColorStyle | Unset
        if isinstance(_negative_color_style,  Unset):
            negative_color_style = UNSET
        else:
            negative_color_style = ColorStyle.from_dict(_negative_color_style)




        _position = d.pop("position", UNSET)
        position: TextPosition | Unset
        if isinstance(_position,  Unset):
            position = UNSET
        else:
            position = TextPosition.from_dict(_position)




        _positive_color = d.pop("positiveColor", UNSET)
        positive_color: Color | Unset
        if isinstance(_positive_color,  Unset):
            positive_color = UNSET
        else:
            positive_color = Color.from_dict(_positive_color)




        _positive_color_style = d.pop("positiveColorStyle", UNSET)
        positive_color_style: ColorStyle | Unset
        if isinstance(_positive_color_style,  Unset):
            positive_color_style = UNSET
        else:
            positive_color_style = ColorStyle.from_dict(_positive_color_style)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        baseline_value_format = cls(
            comparison_type=comparison_type,
            description=description,
            negative_color=negative_color,
            negative_color_style=negative_color_style,
            position=position,
            positive_color=positive_color,
            positive_color_style=positive_color_style,
            text_format=text_format,
        )


        baseline_value_format.additional_properties = d
        return baseline_value_format

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
