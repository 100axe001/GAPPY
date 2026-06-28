from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.color import Color
  from ..models.color_style import ColorStyle





T = TypeVar("T", bound="TreemapChartColorScale")



@_attrs_define
class TreemapChartColorScale:
    """ A color scale for a treemap chart.

        Attributes:
            max_value_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            max_value_color_style (ColorStyle | Unset): A color value.
            mid_value_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            mid_value_color_style (ColorStyle | Unset): A color value.
            min_value_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            min_value_color_style (ColorStyle | Unset): A color value.
            no_data_color (Color | Unset): Represents a color in the RGBA color space. This representation is designed for
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
            no_data_color_style (ColorStyle | Unset): A color value.
     """

    max_value_color: Color | Unset = UNSET
    max_value_color_style: ColorStyle | Unset = UNSET
    mid_value_color: Color | Unset = UNSET
    mid_value_color_style: ColorStyle | Unset = UNSET
    min_value_color: Color | Unset = UNSET
    min_value_color_style: ColorStyle | Unset = UNSET
    no_data_color: Color | Unset = UNSET
    no_data_color_style: ColorStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        max_value_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_value_color, Unset):
            max_value_color = self.max_value_color.to_dict()

        max_value_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.max_value_color_style, Unset):
            max_value_color_style = self.max_value_color_style.to_dict()

        mid_value_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mid_value_color, Unset):
            mid_value_color = self.mid_value_color.to_dict()

        mid_value_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mid_value_color_style, Unset):
            mid_value_color_style = self.mid_value_color_style.to_dict()

        min_value_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_value_color, Unset):
            min_value_color = self.min_value_color.to_dict()

        min_value_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_value_color_style, Unset):
            min_value_color_style = self.min_value_color_style.to_dict()

        no_data_color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_data_color, Unset):
            no_data_color = self.no_data_color.to_dict()

        no_data_color_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_data_color_style, Unset):
            no_data_color_style = self.no_data_color_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_value_color is not UNSET:
            field_dict["maxValueColor"] = max_value_color
        if max_value_color_style is not UNSET:
            field_dict["maxValueColorStyle"] = max_value_color_style
        if mid_value_color is not UNSET:
            field_dict["midValueColor"] = mid_value_color
        if mid_value_color_style is not UNSET:
            field_dict["midValueColorStyle"] = mid_value_color_style
        if min_value_color is not UNSET:
            field_dict["minValueColor"] = min_value_color
        if min_value_color_style is not UNSET:
            field_dict["minValueColorStyle"] = min_value_color_style
        if no_data_color is not UNSET:
            field_dict["noDataColor"] = no_data_color
        if no_data_color_style is not UNSET:
            field_dict["noDataColorStyle"] = no_data_color_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.color import Color
        from ..models.color_style import ColorStyle
        d = dict(src_dict)
        _max_value_color = d.pop("maxValueColor", UNSET)
        max_value_color: Color | Unset
        if isinstance(_max_value_color,  Unset):
            max_value_color = UNSET
        else:
            max_value_color = Color.from_dict(_max_value_color)




        _max_value_color_style = d.pop("maxValueColorStyle", UNSET)
        max_value_color_style: ColorStyle | Unset
        if isinstance(_max_value_color_style,  Unset):
            max_value_color_style = UNSET
        else:
            max_value_color_style = ColorStyle.from_dict(_max_value_color_style)




        _mid_value_color = d.pop("midValueColor", UNSET)
        mid_value_color: Color | Unset
        if isinstance(_mid_value_color,  Unset):
            mid_value_color = UNSET
        else:
            mid_value_color = Color.from_dict(_mid_value_color)




        _mid_value_color_style = d.pop("midValueColorStyle", UNSET)
        mid_value_color_style: ColorStyle | Unset
        if isinstance(_mid_value_color_style,  Unset):
            mid_value_color_style = UNSET
        else:
            mid_value_color_style = ColorStyle.from_dict(_mid_value_color_style)




        _min_value_color = d.pop("minValueColor", UNSET)
        min_value_color: Color | Unset
        if isinstance(_min_value_color,  Unset):
            min_value_color = UNSET
        else:
            min_value_color = Color.from_dict(_min_value_color)




        _min_value_color_style = d.pop("minValueColorStyle", UNSET)
        min_value_color_style: ColorStyle | Unset
        if isinstance(_min_value_color_style,  Unset):
            min_value_color_style = UNSET
        else:
            min_value_color_style = ColorStyle.from_dict(_min_value_color_style)




        _no_data_color = d.pop("noDataColor", UNSET)
        no_data_color: Color | Unset
        if isinstance(_no_data_color,  Unset):
            no_data_color = UNSET
        else:
            no_data_color = Color.from_dict(_no_data_color)




        _no_data_color_style = d.pop("noDataColorStyle", UNSET)
        no_data_color_style: ColorStyle | Unset
        if isinstance(_no_data_color_style,  Unset):
            no_data_color_style = UNSET
        else:
            no_data_color_style = ColorStyle.from_dict(_no_data_color_style)




        treemap_chart_color_scale = cls(
            max_value_color=max_value_color,
            max_value_color_style=max_value_color_style,
            mid_value_color=mid_value_color,
            mid_value_color_style=mid_value_color_style,
            min_value_color=min_value_color,
            min_value_color_style=min_value_color_style,
            no_data_color=no_data_color,
            no_data_color_style=no_data_color_style,
        )


        treemap_chart_color_scale.additional_properties = d
        return treemap_chart_color_scale

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
